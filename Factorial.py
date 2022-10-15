#from LBModule import CheckEvenOdd

def Factorial(iNo):
    for i in range(1,(iNo//2)+1,1): #or for i in range(1,int(iNo/2)+1,1):
        if iNo % i == 0:
            print(i)
    i = 1
    while(i <= int(iNo/2)):
        if iNo % i == 0:
            print(i)
        i = i + 1


def main():
    print("Enter number: ")
    No = int(input())
    Factorial(No)

    ret = CheckEvenOdd(No)


if __name__ == "__main__":
    main()
