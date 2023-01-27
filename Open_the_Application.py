from AppOpener import run
import os
import subprocess

dictionary = {1:"notepad",2:"google chrome",3:"visual studio code",4:"Pycharm Community edition"}
#dictionary2 = {1:"notepad.exe",2:"google chrome",3:"visual studio code",4:"Pycharm Community edition"}

def OpenApplication():
    global dictionary
    no = int(input("Enter application number that you want to open: "))
    if no <= len(dictionary):
        app = dictionary[no]

        run(app)
    else:
        print("Please enter valid number.")

    return
"""
def CloseApplication():
    global dictionary2
    no = int(input("Enter application number that you want to close: "))
    if no <= len(dictionary2):
        app = dictionary2[no]

        subprocess.call("TASKKILL /F /IM {}".format(os.path.abspath(dictionary2[no])), shell=True)
        
    else:
        print("Please enter valid number.")

    return
"""
def Usage():
    print(">> This application is used to open and close the application.")
    print(">> Type 'ls' to list down all the application that you can open and close using this application.")
    print(">> Type 'open' to open the application.")
    #print(">> Type 'close' to close the application.")
    return

def List():
    value = dictionary.values()
    if len(value) > 0:
        print("Below some application you can open.")
        icnt = 0
        for no in value:
            icnt += 1
            print(icnt,":",no)
    else:
        exit()

def main():
    buff = ""
    print("_____________MARVELLOUS INFOSYSTEMS_____________")

    while True:
        buff = input("Marvellous cmd >>")

        if (buff == "open" or buff == "OPEN"):
            List()
            OpenApplication()
            buff = ""
            continue
        """
        if (buff == "close" or buff == "CLOSE"):
            List()
            #CloseApplication()
            buff = ""
            continue
        """
        if (buff == "exit" or buff == "EXIT"):
            print("Thank you for using this application.")
            exit()

        if (buff == "help" or buff == "HELP"):
            Usage()
            continue
        if (buff == "ls" or buff == "LS"):
            List()
            continue
        if (buff == "clear" or buff == "CLEAR"):
            os.system("cls")
            continue
        else:
            print("Invalid command.")
            print("For help type 'help' and press enter.")
            continue

if __name__ == "__main__":
    main()