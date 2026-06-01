class Course:
    def __init__(self, cid, cname):
        self.cid = cid
        self.cname = cname

    def print_info(self, n):
        print(f"Course #{n + 1} information:")
        print('Name: ', self.cname)
        print('Id: ', self.cid)
