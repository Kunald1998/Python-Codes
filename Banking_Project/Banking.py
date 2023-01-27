class BankAccount:
    def __init__(self):
        self.Name = ""
        self.Age = 0
        self.City = ""
        self.Accept_Details()
    
    def Accept_Details(self):
        self.Name = input("Enter your name: ")
        self.Age = int(input("Enter your Age: "))
        self.City = input("Enter your city name: ")
    
    def DisplayInfo(self):
        print("Entered name: ",self.Name)
        print("Entered age: ",self.Age)
        print("Entered city: ",self.City)

def main():

    obj1 = BankAccount()
    #obj1.DisplayInfo()

    #obj2 = BankAccount()
    #obj2.DisplayInfo()

    #obj3 = BankAccount()
    #obj3.DisplayInfo()

    #obj4 = BankAccount()
    #obj4.DisplayInfo()

    # dictx = {AccountNo:object}
    #dictx = {1:obj1, 2:obj2, 3:obj3, 4:obj4}

    #dictx[1].DisplayInfo()
    no = int(input())



if __name__ == "__main__":
    main()