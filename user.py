class User:
    def __init__(self, first_name, last_name):
        self.f_n = first_name
        self.l_n = last_name
    def sayFirst_name(self):
        print(self.f_n)
    def sayLast_name(self):
        print(self.l_n)
    def sayFull_name(self):
        print(self.f_n, self.l_n)
