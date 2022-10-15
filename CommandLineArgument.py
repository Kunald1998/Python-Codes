from sys import *


def Addition(iNo1,iNo2):
    Ans = 0
    Ans = iNo1 + iNo2
    return Ans

def main():
    iRet = 0

    if(len(argv) == 2):
        if((argv[1] == "__u") or (argv[1] == "__U")):
            print("Use this application as:")
            print("python name_of_file first_argv second_argv")

    iRet = Addition(int(argv[1]),int(argv[2]))

    print("Addition is: ",iRet)

if __name__ == "__main__":
    main()
