class Student:
    def __init__(self, sid, sname, sdob):
        self.sid = sid
        self.sname = sname
        self.sdob = sdob

    def print_info(self, n):
        print(f"Student #{n + 1} information:")
        print('Name: ', self.sname)
        print('Id: ', self.sid)
        print('DOB: ', self.sdob)
