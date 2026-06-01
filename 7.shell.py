#!/usr/bin/env python3
"""
A simple Python shell supporting commands, pipes and basic IO redirection.

Usage examples:
  python3 7.shell.py
  pyshell> ls -la
  pyshell> ls -la > out.txt
  pyshell> sort < input.txt
  pyshell> ps aux | grep term

Exit the shell with `exit` or `quit` or Ctrl-D.
"""
import shlex
import subprocess
import sys
from typing import List, Optional


def parse_pipeline(tokens: List[str]):
    """Split tokens into pipeline segments and extract redirections.

    Returns a list of dicts: { 'args': [...], 'stdin': Optional[str], 'stdout': Optional[str] }
    """
    segments: List[List[str]] = []
    cur: List[str] = []
    for t in tokens:
        if t == '|':
            segments.append(cur)
            cur = []
        else:
            cur.append(t)
    if cur:
        segments.append(cur)

    cmds = []
    for seg in segments:
        infile = None
        outfile = None
        args: List[str] = []
        it = iter(seg)
        for tok in it:
            # handle tokens like '>' or '<' and also attached forms like '>out.txt'
            if tok == '>':
                try:
                    outfile = next(it)
                except StopIteration:
                    raise ValueError('No target for output redirection')
            elif tok == '<':
                try:
                    infile = next(it)
                except StopIteration:
                    raise ValueError('No source for input redirection')
            elif tok.startswith('>') and len(tok) > 1:
                outfile = tok[1:]
            elif tok.startswith('<') and len(tok) > 1:
                infile = tok[1:]
            else:
                args.append(tok)

        if not args:
            raise ValueError('Empty command in pipeline')
        cmds.append({'args': args, 'stdin': infile, 'stdout': outfile})

    return cmds


def run_pipeline(cmds):
    procs = []
    open_files = []
    prev_stdout = None

    for i, cmd in enumerate(cmds):
        stdin = None
        stdout = None

        if cmd['stdin'] is not None:
            f = open(cmd['stdin'], 'rb')
            open_files.append(f)
            stdin = f
        elif prev_stdout is not None:
            stdin = prev_stdout

        if cmd['stdout'] is not None:
            f = open(cmd['stdout'], 'wb')
            open_files.append(f)
            stdout = f
        elif i < len(cmds) - 1:
            # create a pipe for the next process
            stdout = subprocess.PIPE

        try:
            p = subprocess.Popen(cmd['args'], stdin=stdin, stdout=stdout, stderr=subprocess.PIPE)
        except FileNotFoundError:
            # clean up opened files and processes
            for f in open_files:
                try:
                    f.close()
                except Exception:
                    pass
            for pp in procs:
                pp.wait()
            print(f"Command not found: {cmd['args'][0]}")
            return

        procs.append(p)

        # set prev_stdout to the pipe end we will use as stdin for next proc
        if p.stdout is not None:
            prev_stdout = p.stdout
        else:
            prev_stdout = None

    # collect output from the last process if not redirected to file
    last = procs[-1]
    out, err = last.communicate()

    # close any files we opened
    for f in open_files:
        try:
            f.close()
        except Exception:
            pass

    # print stderr if any
    if err:
        try:
            sys.stderr.write(err.decode('utf-8'))
        except Exception:
            sys.stderr.write(str(err))

    # if last.stdout was a pipe, print captured output
    if last.stdout is None or last.stdout == subprocess.PIPE:
        if out:
            try:
                sys.stdout.write(out.decode('utf-8'))
            except Exception:
                sys.stdout.write(str(out))


def main():
    try:
        while True:
            try:
                line = input('pyshell> ')
            except EOFError:
                print()  # newline after Ctrl-D
                break

            line = line.strip()
            if not line:
                continue
            if line in ('exit', 'quit'):
                break

            try:
                tokens = shlex.split(line)
            except ValueError as e:
                print(f'Parse error: {e}')
                continue

            # support simple 'cd' builtin
            if tokens[0] == 'cd':
                try:
                    target = tokens[1] if len(tokens) > 1 else None
                    if target:
                        import os

                        os.chdir(target)
                    else:
                        import os

                        os.chdir(os.path.expanduser('~'))
                except Exception as e:
                    print(f'cd: {e}')
                continue

            try:
                cmds = parse_pipeline(tokens)
            except ValueError as e:
                print(f'Error: {e}')
                continue

            run_pipeline(cmds)
    except KeyboardInterrupt:
        print()  # newline and exit


if __name__ == '__main__':
    main()
