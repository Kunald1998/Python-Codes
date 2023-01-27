import sys

print(sys.getrecursionlimit()) #output =  1000
sys.setrecursionlimit(3001) # Here we set random value for recursion.
print(sys.getrecursionlimit()) # output = 3001

def demo(No):
    if (No > 0):
        print("Hello ")
        No = No - 1
        demo(No) # Recursive function call. # This is a tail recursion. because function call is written at the end of method.

def main():
    no = int(input("Enter number: "))
    demo(no)

if __name__ == "__main__":
    main()