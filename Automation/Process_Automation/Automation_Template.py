from sys import *

def Script_Task(No):
    pass
    # HERE COMES LOGIC OF TASK THAT WE WANT TO DO.


def Display_On_Terminal():
    print("----------Marvellous Infosystems Automation--------------")

    print("Automation script started with the file name: ", argv[0])

    if (len(argv) != 2):
        print("Error: Insufficient arguments.")
        print("Use '-h' for help and '-u' for usage of this script.")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help: This script is used to perform______________.")
        exit()

    if ((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage: Provide_______number of arguments as.")
        print("First argument as:________")
        print("Second argument as:_________")
        exit()

    else:
        Script_Task(int(argv[1]))


def main():
    Display_On_Terminal()

if __name__ == "__main__":
    main()
