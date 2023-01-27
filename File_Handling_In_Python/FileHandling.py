def main():

    Filex = open(file="marvellous.txt",mode="r")
    print("Information about file is: ",Filex)
    print("data from file is: ",Filex.read())

    print("Read first line from file: ",Filex.readline()) # Here we do not get any output because cursor is at last position of file.
    print("Current position of cursor is: ",Filex.tell()) # This method tells that what is your current position of cursor.
    Filex.seek(0) # Due to this we shift the cursor to the first position.
    print("Read first line from file: ", Filex.readline()) # now we get the output bcoz cursor is at initial position.
    print("Content of whole file is: ",Filex.read())

    Filex.close() # due to this we close the file.

    # print("Data: ",Filex.read()) this gives error bcoz our file is closed.

    Filex = open(file="marvellous.txt",mode="a")

    Filex.write("Python:Guido van Rosuum\n")
    Filex.write("C: Dennis Ritchi\n")
    Filex.seek(0)

    print("Data after writing is: ",Filex.read())

    Filex.close()


if __name__ == "__main__":
    main()


