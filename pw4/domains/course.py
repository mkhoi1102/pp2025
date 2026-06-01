class Course:
    def __init__(self, cid, cname, credits=1):
        self.cid = cid
        self.cname = cname
        self.credits = credits

    def print_info(self, n):
        print(f"Course #{n + 1} information:")
        print('Name: ', self.cname)
        print('Id: ', self.cid)
        print('Credits: ', self.credits)
