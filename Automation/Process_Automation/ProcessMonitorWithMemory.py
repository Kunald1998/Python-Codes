import psutil
from psutil import *
def Process_Display():
    ListOfProcess = []

    for Process in psutil.process_iter():
        try:
            Proinfo = Process.as_dict(attrs=['pid','name','username'])
            Proinfo['VMS'] = Process.memory_info().vms/(1024*1024)
            ListOfProcess.append(Proinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return ListOfProcess

def main():
    print("Marvellous Infosystems: Python Automation & Machine Learning.")

    print("Process Monitor.")

    ListProcess = Process_Display()

    for element in ListProcess:
        print(element)

if __name__ == "__main__":
    main()