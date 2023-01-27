import os
def Read_File(FileName):
    if(os.path.exists(FileName)):
        fd = open(file=FileName,mode="r")
        print("Data from file is: ",fd.read())
        fd.close()
    else:
        print("File is not present.")
        exit()

def main():
    print("Enter the file name to create: ")
    Name = input()

    Read_File(Name)

if __name__ == "__main__":
    main()