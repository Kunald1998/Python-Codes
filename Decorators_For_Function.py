import Decorator_Required_Function as DRF

def Decoratorforsub(Function_Name): #200
    def Inner1(no1,no2): #300
        print("ID inside Inner1 is: ", id(Inner1))
        if(no1<no2):
            no1,no2 = no2,no1 # This is multi-assignment statement. and we use swapping.
        ret = Function_Name(no1,no2)
        return ret

    return Inner1 # return(300)

def Decoratorfordivision(Function_Name): #400
    def Inner2(no1,no2): #500
        print("ID inside Inner1 is: ",id(Inner2))
        if(no1 < no2):
            no1,no2 = no2,no1
        ret = Function_Name(no1,no2)
        return ret

    return Inner2 # return (500)

def main(): # 100
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))

    NewFunction1 = Decoratorforsub(DRF.Substraction) # NewFunction1 = call(200,function_Name_string)
    print("Type of NewFunction1 is: ",type(NewFunction1))
    print("ID of the inner1 function is: ",id(NewFunction1))
    # Here NewFunction1 contain Function name as 'Inner1'.

    Value1 = NewFunction1(No1,No2) # value1 = call(300,No1,No2)
    print("Substraction of (larger - smaller) is: ",Value1)



    NewFunction2 = Decoratorfordivision(DRF.Division) # NewFunction2 = call(400,function_Name_string)
    print("Type of NewFunction2 is: ", type(NewFunction2))
    print("ID of the inner2 function is: ", id(NewFunction2))
    # Here NewFunction2 contain Function name as 'Inner2'.

    Value2 = NewFunction2(No1,No2) # Value2 = call(500,No1,No2)
    print("Division of (bigger / smaller) is: ",Value2)


if __name__ == "__main__":
    main() # call(100)

"""
OUTPUT
Enter first number: 2
Enter second number: 10
Type of NewFunction1 is:  <class 'function'>
ID of the inner1 function is:  2201771376448 # same
ID inside Inner1 is:  2201771376448 # same
Substraction of (larger - smaller) is:  8

Type of NewFunction2 is:  <class 'function'>
ID of the inner2 function is:  2201771475008 # same
ID inside Inner1 is:  2201771475008 # same
Division of (bigger / smaller) is:  5.0


"""