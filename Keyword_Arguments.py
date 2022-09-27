print("Demonstration of keyword arguments for a functions.")

def batches(name,fees):

    print("Name of batch is: ",name)
    print("Fees of the batch is: ",fees)

def main():
    batches(name="Python",fees=16500) # We can send parameter in correct order format.
                                                    # or
    batches(fees=15000,name="Angular") # We can send parameter in randon format.

if __name__=="__main__":
    main()