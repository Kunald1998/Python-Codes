import os
def Write_into_File(FileName):
    if(os.path.exists(FileName)):
        print("Enter the data that you want to write into a the file.")
        Data = input()
        fd = open(file=FileName,mode="a")
        fd.write(Data)
    else:
        print("File is not existing.")
        return

def main():
    print("Enter the file name to create: ")
    Name = input()

    Write_into_File(Name)

if __name__ == "__main__":
    main()