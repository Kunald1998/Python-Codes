import os
from sys import *

def Directory_Watch(Dir_Name):
    print("Inside Directory watcher method.")
    print("Name of input directory is: ",Dir_Name)

    for foldername, subfolder, Filenames in os.walk(Dir_Name):
        print("Folder name is: ",foldername)
        for subf in subfolder:
            print("Subfolder name of: "+foldername+"is"+subf)
        for fname in Filenames:
            print("File inside folder"+foldername+"is"+fname)

        print(" ")

def main():
    print("Enter name of directory: ")
    if(len(argv) < 1):
        print("Insufficient arguments.")
        exit()

    if((argv[1] == "-h")or(argv[1] == "-H")):
        print("This script will display and display the name of all entries.")
        exit()

    if ((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage: Application_name Directort_name.")
        exit()

    Directory_Watch(argv[1])


if __name__ == "__main__":
    main()