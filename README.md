# USTH Advanced Python 2025

ID: 23BI14229
Name: Dang Minh Khoi
ICT Class 1

## Practical work 7: Python shell

This repository contains a small interactive Python shell `7.shell.py` that supports:

- running external commands
- simple pipelines using `|`
- basic input `<` and output `>` redirection
- a `cd` builtin and `exit`/`quit` to leave the shell

Quick start:

```bash
python3 7.shell.py
# then try:
pyshell> ls -la
pyshell> ls -la > out.txt
pyshell> sort < input.txt
pyshell> ps aux | grep python
```

Notes:
- The parser supports both separated redirection tokens (`> out.txt`) and attached forms (`>out.txt`).
- This is a teaching/demo shell; it does not implement job control, backgrounding, complex quoting corner-cases, or advanced shell features.
