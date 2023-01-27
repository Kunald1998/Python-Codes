def main():
    try:
        print("Enter first number: ")
        No1 = int(input())
        print("Enter second number:")
        No2 = int(input())

        Ans = No1/No2 # this line is exception prone code.
        print("Division is: ",Ans)

    # If we provide '0' value for No2 variable then zeroDivisionError occurs.
    # Mathematicaly if we divide any number by zero then it given infinite values thats why...
     
    except ZeroDivisionError:
        print("Inside zero division error.")

    # If we provoide character insted of number for No1 or No2 in above inputs then ValueError occurs.
    except ValueError:
        print("inside value error.") 

    except Exception:
        print("Inside last exception block.")

    finally: # this block is execute every time.
        print("Inside finally block.")

if __name__ == "__main__":
    main()

"""
 if __name__ == "__main__":
SyntaxError: expected 'except' or 'finally' block  

# The above error proves that python is compiled + interpreted.
# Because the word SyntaxError shows the first python program is get compiled and then it gets convert it into the byte code.
# Byte code is only created if our program contains no syntax error.
"""
