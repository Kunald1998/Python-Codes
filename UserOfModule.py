import Module # here we import Module.py file
def main():

    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    ret = 0

    ret = Module.add(value1,value2)
    print("Addition is: ",ret)

    ret = Module.sub(value1,value2)
    print("Substraction is: ",ret)

    ret = Module.mult(value1,value2)
    print("Multiplication is: ",ret)

if __name__=="__main__":
    main()
