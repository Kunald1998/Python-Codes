import os,time

def Create_LogFile(Arrayx,Titlex,Direct_Name):
    try:
        os.mkdir(Direct_Name)

    except(FileExistsError, FileNotFoundError, NotADirectoryError):
        pass

    pathx = os.path.join(Direct_Name,"Marvellouslog%s.log"%time.time())

    fd = open(file=pathx,mode="w")

    decorators = "-" * 80

    fd.write(decorators + "\n")
    fd.write("This log file is use to store the information about"+" "+ Titlex +"\n")
    fd.write(">>>This log file is created at: " +time.ctime()+ "<<<"+"\n")
    fd.write(decorators + "\n")

    if (len(Arrayx)>0):
        for info in Arrayx:
            fd.write("%s \n" % info)
    else:
        print("There is no data to store into the log file.")

    fd.close()