from functools import reduce

Multiply = lambda No : (No * 2)

"""def Multiply(iNo):
    return (iNo * 2)"""

CheckEven = lambda No : (No % 2 == 0)

"""def CheckEven(iNo):
    return (iNo % 2 == 0)"""

Sum = lambda Ans,No : (Ans+No)

"""def Sum(A,B):
    return A+B"""


def main():
    Data_Input = []

    print("Enter the size of list: ",end="")
    iSize = int(input())

    print("Please enter the data: ")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is: ",Data_Input)

    Data_Filter = list(filter(CheckEven,Data_Input))
    print("Data after Filter is: ",Data_Filter)

    Data_Map = list(map(Multiply,Data_Filter))
    print("Data after Mapping is: ",Data_Map)

    Data_Reduce = reduce(Sum,Data_Map)
    print("Result after reduce is:",Data_Reduce)


if __name__ == "__main__":
    main()