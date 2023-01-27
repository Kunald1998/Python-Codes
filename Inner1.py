# Demonstration of calling function which is inside another function.

def Outer():   #100
    print("Inside outer.")

    def Inner():   #200
        print("Inside Inner.")
    print(id(Inner))
    return Inner   # here ID is return.  # return 200

ret = Outer()   # ret madhe Inner asa nav ala.
print(type(ret))
print(id(ret))
ret()    # this is convert into Inner() # 200()