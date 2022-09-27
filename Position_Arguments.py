from traceback import print_tb


print("Demonstration of positional or required arguments for a function.")

def batches(name,fees): 

    print("Batch name is: ",name)
    print(type(name))
    
    print("fees for that batch is: ",fees)
    print(type(fees))

def main():
    batches("Python",16500) # Due to this in name = Python and fees = 16500.

    batches(15000,"Angular") # Due to this in name = 15000 and fees = Angular.

    # batches(15000) this is not accepted.

if __name__=="__main__":
    main()


"""
Output=

Batch name is:  Python
<class 'str'>
fees for that batch is:  16500
<class 'int'>
Batch name is:  15000
<class 'int'>
fees for that batch is:  Angular
<class 'str'>
"""
