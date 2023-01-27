import os
import platform
import wmi # install this module using pip command.
import psutil # install this module using pip command.
import urllib.request
"""
Add some functions like type of RAM/HHD

"""
def main():
    Decorator1 = ">" * 20
    Decorator2 = "<" * 20
    seperator = "-" * 80
    print(Decorator1 + "INFORMATION ABOUT MY MACHINE ARE GIVEN BELOW" + Decorator2)

# --------------------------------Computer_info-------------------------------------------
    my_system = ""
    try:
        obj = wmi.WMI()
        my_system = obj.Win32_ComputerSystem()[0]
    except(ModuleNotFoundError,TypeError):
        print("Please import 'wmi' module. To import use below command:")
        print("pip install wmi")

    print("Computer manufacturer is: ",my_system.Manufacturer)
    print("Model name is: ",my_system. Model)
    print("System family: ",my_system.SystemFamily)

#-------------------------------Architecture_Info---------------------------------
    print(seperator+"\n")

    print("Number of processor in this machine is: ",my_system.NumberOfProcessors)
    print("Name of the processor is: ",platform.processor())
    print("System type:",my_system.SystemType)
    print("Machine is: ", platform.machine())
    print("Number of core present in microprocessor is: ", os.cpu_count())

    Count1 = ""
    Count2 = ""
    try:
        Count1 = psutil.cpu_count(logical=False)
        Count2 = psutil.cpu_count(logical=True)
    except(ModuleNotFoundError, NameError):
        print("Please import 'psutil' module. To import use below command.")
        print("pip install psutil")

    print("Physical cores is:", Count1)
    print("complete phisical and logical cores is:", Count2)

#-------------------------------Platform_Info-----------------------------------------
    print(seperator+"\n")
    print("Name of the Operating-System is: ", platform.system())
    print("Version of the operating system is: ", platform.version())
    print("Architecture configuration and file file format is: ", platform.architecture())

#---------------------------Internet_Connection_Check-----------------------------------------

    def connect():
        try:
            urllib.request.urlopen('http://google.com')
            return True
        except:
            return False

    ret = connect()
    if(ret == True):
        print("Machine is 'Connected' to the internet.")
    else:
        print("Machine is 'Not Connected' to the internet.")

#-----------------------------------Cup_Usage----------------------------------------------
    print('The CPU usage is: ',psutil.cpu_percent(10),"%") # 10 is the seconds for that time python code calculate the CPU percentage.

# ---------------------------Memory_Info_Ram_&_HHD-----------------------------------------

    size = psutil.virtual_memory().total/1024**3
    print("Size of RAM is:",size,"GB")

    hdd = psutil.disk_usage('/')
    print("Size of C:Drive: ",hdd.total / (2 ** 30),"GB")
    print("Used size is:",hdd.used / (2 ** 30),"GB")
    print("Free size is:", hdd.free / (2 ** 30),"GB")

if __name__ == "__main__":
    main()