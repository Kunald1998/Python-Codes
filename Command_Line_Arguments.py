from ast import arg
import sys

print("Demonstration of command line arguments.")

def add(no1,no2):
    ans = 0
    ans = no1 + no2
    return ans

def main():

    print("Application name is: ",sys.argv[0]) 
    print("Application name is: ",sys.argv[1])
    print("Application name is: ",sys.argv[2])

    print("Length of the argv array is: ",len(sys. argv)) # This method will return the length of command that you will provide at the time of give the command.

    ret = add(int(sys.argv[1]),int(sys.argv[2])) # argv is a array name which contains commands.

    print("Addition is: ",ret)

if __name__=="__main__": # User defined entry point function.
    main()


# To run the above code use this command :- [python_CommandLine.py_10_11]  ['_' this is a space.] 10 and 11 are the parameters for addition.
# As command is considered as a array of vector in our above command, file name is at 0th index and 10 is at 1st index and 11 is at 2nd index.