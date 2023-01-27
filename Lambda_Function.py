# Lambda Functions/ Unnamed function
# Prototype of lambda function is:=  lambda parameters : body
# Addfunction = lambda A,B : A+B

CheckEvenOdd = lambda No : (No % 2 == 0) # labda function.

Ret = CheckEvenOdd(13) # call to the lambda function.

print(Ret)

if(Ret == True):
    print("Number is even")
else:
    print("Number is odd")