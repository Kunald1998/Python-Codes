import psutil # process and system utilities = psutil

def Process_Display():
    ListOfProcess = []

    for Process in psutil.process_iter():
        try:
            Proinfo = Process.as_dict(attrs=['pid','name','username'])
            ListOfProcess.append(Proinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return ListOfProcess

def main():
    print("Process Monitor.")

    ListProcess = Process_Display()

    for element in ListProcess:
        print(element)

if __name__ == "__main__":
    main()