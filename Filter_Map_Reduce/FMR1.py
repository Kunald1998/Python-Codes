# This code does not contain helper functions for filter,map & reduce.
def FILTERCheckOdd(Arr):
    Brr = list()
    for i in Arr:
        if(i % 2 != 0):
            Brr.append(i)
    return Brr

def MAPAddOdd(Arr):
    for i in range(0,len(Arr),1):
        Arr[i] = Arr[i] + 1
    return Arr

def REDUCEAddallOdd(Arr):
    sum = 0
    for i in Arr:
        sum = sum + i
    return sum


def main():
    Array = [1,3,4,10,12,15,17,20]
    print("Array before filter is: ",Array)

    FilterArray = FILTERCheckOdd(Array)
    print("Filtered array is:",FilterArray)

    MapArray = MAPAddOdd(FilterArray)
    print("Array after mapping is: ",MapArray)

    ReduceArray = REDUCEAddallOdd(MapArray)

    print("Array after reduce is: ",ReduceArray)

if __name__ == "__main__":
    main()