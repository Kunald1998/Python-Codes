# THIS CODE IS BELONGS TO PIYUSH KHAIRNAR SIR.
def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return (No + 2)

def FilterX(Arr,Function_Name):
    Result = []
    for no in Arr:
        if(Function_Name(no)):
            Result.append(no)
    return Result


def mapX(Arr,Function_Name):
    Result = []
    for no in Arr:
        value = Function_Name(no)
        Result.append(value)
    return Result

def ReduceX(Arr):
    Sum = 0
    for no in Arr:
        Sum = Sum + no
    return Sum


def main():
    Data = [2,3,1,6,4,5,11,16,20]

    Data_Filter = list(FilterX(Data,CheckEven))
    print(Data_Filter)

    Data_map = list(mapX(Data_Filter,Increment))
    print("Data after map: ",Data_map)

    Ret = ReduceX(Data_map)
    print("Data after reduce is:",Ret)

if __name__ == "__main__":
    main()