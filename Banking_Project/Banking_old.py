# Instance variable: Name,Amount,Address,AccountNo.
# Instance method: CreateAccount(),DisplayAccountInfo(),
# Class variable: Bank_Name, ROI_On_FD,
# Class method: DisplayBankInformation(),
# Static method: DisplayKYCInfo()
class Bank_Account:

    Bank_Name = "HDFC Bank PVT LTD." # class variable
    ROI_On_FD = 6.7 # class variable

    def __init__(self): #Below Name,Amount,Address,AccountNo are instace variables.
        self.Name = ""
        self.Amount = 0.0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name: ")
        self.Name = input()

        print("Enter your initial amount: ")
        self.Amount = float(input())

        print("Enter your address: ")
        self.Address = input()

        print("Enter your Account Number: ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("----------YOUR ACCOUNT INFORMATION IS AS BELOW----------")
        print("Your name is: ",self.Name)
        print("Your Bank balance is: ",self.Amount)
        print("Your Entered address is: ",self.Address)
        print("Your Account number is: ",self.AccountNo)

    
    @classmethod
    def DisplayBankInformation(cls): # Class method
        print("Welcome to banking console.")
        print("Name of bank is: ",cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposits is: ",cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC information.")
        print("According to the rules of goverment of india you have to submit below documents.")
        print("1: CLear and recent passportsize photo.")
        print("2:photo and aadhar card.")
        print("3: Photo of PAN card.")
    
    def Deposit(self,Value):
        self.Amount = self.Amount + Value

    def Withdraw(self,value):
        self.Amount = self.Amount - value


def main():

    #print("Name of bank: ",Bank_Account.Bank_Name)
    #print("Rate of intrest on fixed deposit :",Bank_Account.ROI_On_FD)
    Bank_Account.DisplayKYCInfo()
    Bank_Account.DisplayBankInformation() # Calling the class method without creating the object of a class.
    # Bank_Account.CreateAccount() This is not allowed.
    User1 = Bank_Account() # Creating the object of class.
    User2 = Bank_Account()
    
    print("Creating the first account.")
    User1.CreateAccount()
    print("Creating the second account.")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__ == "__main__":
    main()