def Substraction(No1,No2): # Assume that this method is written by another developer.
# We are not able to change any parameter inside the substraction method.
    Ans = 0
    Ans = No1 - No2
    return Ans
# Below all is concept of Decorator of another function.
def Decorated_Function(Function_Name):
    def Inner(A,B):
        if(A < B):
            A,B = B,A # Multi assignment statement.This is swapping.
        output = Function_Name(A,B)
        return output

    return Inner

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    New_Function = Decorated_Function(Substraction)
    ret = New_Function(value1,value2)
    print("Substraction is: ",ret)

if __name__ == "__main__":
    main()