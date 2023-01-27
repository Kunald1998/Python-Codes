import threading
import time
import os

def DisplayEven(No):
    
    for i in range(No):
        if i % 2 == 0:
            print("Even numbers are: ",i)

def DisplayOdd(No):
    for i in range(No):
        if i % 2 != 0:
            print("Odd numbers are: ",i)
    

def main():
    Number = 200

    T1 = threading.Thread(target=DisplayEven,args=(Number,))
    T2 = threading.Thread(target=DisplayOdd,args=(Number,))

    T1.start()
    T2.start()
    
    T1.join()
    T2.join()

if __name__ == "__main__":
    print("Current process ID is: ",os.getpid())
    print("Parent  process ID is: ",os.getppid())
    
    Start = time.process_time()
    main()
    End = time.process_time()
    print("Total execution time is: ",End - Start)