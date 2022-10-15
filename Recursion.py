def RecursionInPython(iNo):
    if(iNo > 0):
        print("Jay Ganesh...")
        iNo = iNo - 1
        RecursionInPython(iNo)

def main():
    print("Enter number: ")
    value = int(input())
    RecursionInPython(value)

if __name__ == "__main__":
    main()