import os

def main():
    print("PID of current process is : ",os.getpid()) # current process chi id bhetate. This python program.
    print("PID of parent process is : ",os.getppid()) # Parent process chi id kadhun dete. command prompt.

if __name__ == "__main__":
    main()

"""
OUTPUT
PID of current process is :  13616
PID of parent process is :  12612  This number is belong to Command prompt bcoz we run our code on cmd process.

PID of current process is :  10896
PID of parent process is :  12612 this number is same.

Above numbers are different for each Operating system.
These numbers are different for every time.

"""