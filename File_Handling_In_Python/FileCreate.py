import os
def Create_File(FileName):
    if (os.path.exists(FileName)): # This is use to check file is already present or not.
        print("File is already exist.")
        exit()
    else:
        fd = open(file=FileName, mode="w")

def main():
    print("Enter the file name to create: ")
    Name = input()

    Create_File(Name)

if __name__ == "__main__":
    main()