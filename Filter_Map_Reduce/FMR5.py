from functools import reduce
CheckEven = lambda No: (No % 2 == 0) # For filter method.


SquareValue = lambda No : (No ** 2)# for map method.

AddValues = lambda No1,No2 : (No1 + No2) # for reduce method.

def AcceptList():
    List = []

    print("Enter how many element you want to store: ", end="")
    iSize = int(input())

    print("Please enter the elements of list: ")
    for i in range(0, iSize, 1):
        no = int(input())
        List.append(no)
    return List

def main():
    ListData = AcceptList()

    # 1st Approach of 'Canonical' function call.
    Output = reduce(AddValues,map(SquareValue,(filter(CheckEven,ListData))))
    print("Data after reduce is: ",Output)

    # 2nd Approach of 'Canonical' function call.
    #Output = reduce(lambda No1,No2 : (No1 + No2), map(lambda No : (No ** 2), (filter(lambda No: (No % 2 == 0), ListData))))
    #print("Data after reduce is: ",Output)

    # 3rd Approach of 'Canonical' function call.
    #print("Reduced data is: ",reduce(lambda No1,No2 : (No1 + No2), map(lambda No : (No ** 2), (filter(lambda No: (No % 2 == 0), ListData)))))

if __name__ == "__main__":
    main()