import os
import psutil
import time
from sys import *

def Process_Display(Log_Dir = "Marvellous"):
    ListOfProcess = []
    
    if not os.path.exists(Log_Dir):
        try:
            os.mkdir(Log_Dir)
        except:
            pass
    
    Seperator = "_" * 80
    Log_Path = os.path.join(Log_Dir,"Current_Running_Process_Log.log")
    fd = open(Log_Path,'w')
    fd.write(Seperator + "\n")
    fd.write("Process Logger Time: "+time.ctime() + "\n")
    fd.write(Seperator + "\n")

    for Process in psutil.process_iter():
        try:
            Proinfo = Process.as_dict(attrs=['pid','name','username'])
            Proinfo['VMS'] = Process.memory_info().vms/(1024*1024)
            ListOfProcess.append(Proinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    for element in ListOfProcess:
        fd.write("%s\n" % element)

def main():
    print("Application name is: ",argv[0])

    if(len(argv) != 2):
        print("Error: Invalid number of argumnets.")
        exit()

    if((argv[1] == "-h")or(argv[1] == "-H")):
        print("This script is used log record of running processess.")
        exit()
    if((argv[1] == "-u")or(argv[1] == "-U")):
        print("Usage: Application Absolute path of Directory.")
        exit()
    try:
        Process_Display(argv[1])

    except(ValueError):
        print("Error: Invalid datatype of input.")
    except(Exception):
        print("Error: Invalid Input.")

if __name__ == "__main__":
    main()