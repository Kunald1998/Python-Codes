# In this code we import "Marvellous module" Marvellous_Module is a another .py file which is act like a module  file.

import Marvellous_Module

def main():
    print("Value of __name__ from main function is: ",__name__) # This will show which is a main file, from where the program will start.
    print("Enter first number: ")
    no1 = int(input())
    print("Enter second number: ")
    no2 = int(input())

    Ret = Marvellous_Module.Addition(no1,no2)
    print("Addition is: ",Ret)

if (__name__ == "__main__"):
    main() 