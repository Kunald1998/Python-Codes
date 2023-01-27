import os
def Delete_File_Check(FileName):
    if(os.path.exists(FileName)):
        size = os.path.getsize(FileName)
        if(size != 0):
            print("are you sure to delete the file? Y/N")
            option = input()
            if((option == "Y")or(option == "y")):
                os.remove(FileName)
                print("File is deleted.")
            if((option == "N")or(option == "n")):
                print("File deletion process is stoped.")
                return
        else:
            os.remove(FileName)
            return
    else:
        print("There is no such a file present in the directory.")

def main():
    print("Enter the file name that you want to delete: ",end="")
    Name = input()
    Delete_File_Check(Name)

if __name__ == "__main__":
    main()