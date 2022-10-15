# In this module I am going to add all logic bulding problems.

                                                # PATTERN PRINTING

def PatternPrint1(Row,Col):
    if(Row < 0):
        print("Please enter positive value.")
        Row = - Row
    elif (Col < 0):
        print("Please enter positive value.")
        Col = - Col

    for irow in range(0,Row,1):
        for icol in range(0,Col,1):
            print(" * ",end= "")
        print("")


                                                # PROBLEMS ON NUMBERS

def Factorial(iNo):
    for i in range(1,(iNo//2)+1,1): # or for i in range(1,int(iNo/2)+1,1):
        if iNo % i == 0:
            print(i)
    i = 1
    while(i <= int(iNo/2)):
        if iNo % i == 0:
            print(i)
        i = i + 1

def CheckEvenOdd(No):
    if(No %  2 == 0):
        print("Given number is Even number.")
    else:
        print("Given number is Odd number.")

def CheckPrime(No):
    if(No < 0):
        No = -No
    Fact = 0
    for i in range(1,No,1):
        if (No % i == 0):
            Fact = Fact + 1

    if (Fact > 2):
        print("Given number is not a prime number.")
    else:
        print("Given number is a prime number.")

def CheckPerfect(No):
    if(No < 0):
        No = -No
    Sum = 0

    for i in range(1,No,1):
        if No % i == 0:
            Sum = Sum + i

    if (No == Sum):
        print("The given number is perfect number.")
    else:
        print("Given number is not perfect number.")

def CheckPalindrome(No):
    x = 0
    temp = No
    while(No != 0):
        x = x * 10 + (No % 10)
        No = int(No / 10)

    if(temp == x):
        print("Given number is Palindrome number.")
    else:
        print("Given number is not a palindrome number.")


def DisplayEven(Brr = list()):
    end = len(Brr)
    print("Even number are: ")
    for i in range(0,end,1):
        if(Brr[i] % 2 == 0):
            print(Brr[i],end = " ")

def DisplayOdd(Brr = list()):
    end = len(Brr)
    print("Odd number are: ")
    for i in range(0,end,1):
        if(Brr[i] % 2 != 0):
            print(Brr[i],end = " ")


                                                # PROBLEMS ON STRINGS

def CountUpperLowerCase(string):
    Arr = list(string)
    print(Arr)
    iCntU = 0
    iCntL = 0
    for i in range(0,len(string),1):

        if((Arr[i] >= 'A')and(Arr[i] <= 'Z')):
            iCntU += 1
        elif ((Arr[i]) >= 'a')and((Arr[i]) <= 'z'):
            iCntL += 1

    return iCntU,iCntL

def DisplayFrequency(string):
    Arr = list(string)
    dictionaryX = {}
    freq = 0
    for i in range(0,len(Arr),1):
        freq = 0
        for j in range(0,len(Arr),1):
            if(Arr[i] == Arr[j]):
                freq = freq + 1
        
        dictionaryX[Arr[i]] = freq
    
    return dictionaryX


def ChangeCaseUpper(string):
    Arr = list(string)
    
    for i in range(0,len(Arr),1):
        if((Arr[i] >= 'a')and(Arr[i] <= 'z')):
            chrx = ord(Arr[i]) #The ord() function returns ASCII value of character passed as its argument.
            chrx = chrx - 32
            Arr[i] = chr(chrx) # The chr() function returns corresponding character of ASCII value passed as its argument. 
    value = ""
    value = value.join(Arr) # The join() method join each element from list to each other and store in 'value' variable.
    return value

def ChangeCaseLower(string):
    Arr = list(string)

    for i in range(0,len(Arr),1):
        if((Arr[i] >= 'A')and(Arr[i] <= 'Z')):
            chrx = ord(Arr[i]) #The ord() function returns ASCII value of character passed as its argument.
            chrx = chrx + 32
            Arr[i] = chr(chrx) # The chr() function returns corresponding character of ASCII value passed as its argument. 
    value = ""
    for i in Arr:
        value = value + i    # Here we add each element from list with each other and store in value variable.

    return value

def ChecklengthofString(string):
    print(len(string))
    name = ""
    name = string.replace(" ","")
    print(name)
    print(len(name))


def main():

    print("Enter string: ")
    name = input()
    ChecklengthofString(name)
    
    

if (__name__ == "__main__"):
    main()