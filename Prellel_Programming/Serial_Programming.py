print("Demonstration of serial programming.")
import time
import os
def DisplayEven(No):
    print("Even numbers are:")
    for i in range(No):
        if i % 2 == 0:
            print(i," ")

def DisplayOdd(No):
    print("Odd numbers are:")
    for i in range(No):
        if i % 2 != 0:
            print(i," ")

def main():
    Number = 100
    DisplayEven(Number)
    DisplayOdd(Number)

if __name__ == "__main__":
    print("Serial_Programming Program process ID is: ",os.getpid()) # This ID is belongs to my this file which get convert it into process.
    print("Parent process id is: ",os.getppid()) # This ID is belongs to command prompt CMD, because we run our program on current running programm of command prompt.
    # Command prompt is a program if we run cmd.exe file then it will become a process.
    Start = time.process_time()
    main()
    end = time.process_time()
    print("execution time required is: ",end-Start)

"""
In this program first DisplayEven method is get called and then DisplayOdd method is get called in serial manner
because of the top to buttom approach of python.

"""