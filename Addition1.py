print("Application to demonstrate industrial programming.")

def main():
    print("Enter first number: ")
    no1 = input()

    print(type(no1))
    print("Enter second number: ")

    no2 = input()
    print(type(no2))

    ans = int(no1) + int(no2)  # Do it like this, not like this no1 = int(input())

    # When you want a variable in integer format in whole program then, no1 = int(input()) it is usefull.

    print("Addition is: ",ans)

if (__name__ == "__main__"):
    main()