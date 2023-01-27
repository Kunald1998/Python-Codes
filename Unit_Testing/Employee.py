class Employe:
    raise_amt = 1.05

    def __init__(self,first,last,pay):
        self.First = first
        self.Last = last
        self.Pay = pay
    
    @property
    def email(self):
        return("{}.{}@email.com".format(self.First,self.Last))
    
    @property
    def Fullname(self):
        return("{} {}".format(self.First,self.Last))

    def Apply_Raise(self):
        self.Pay = int(self.Pay * self.raise_amt)
        