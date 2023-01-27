import os
import re
import webbrowser
from sys import *
import urllib.request

def OpenURL(URL):
    for urls in URL:
        webbrowser.open_new_tab(urls)
    return

def FindUrl(line):
    # USE ANOTHER REGEX FOR CHECK URL.
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, line)
    return url

def OpenFile(filename):
    flag = os.path.isabs(filename)
    if flag == False:
        filename = os.path.abspath(filename)
    exist = os.path.isfile(filename)

    if exist:
        fd = open(file=filename, mode="r")
        for line in fd:
            UrlList = FindUrl(line)
            for url in UrlList:
                OpenURL(url)
    else:
        print("Invalid path.")

def CheckInternetConnection():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

def main():
    print("------------MARVELLOUS INFOSYSTEMS------------")
    print("Application name is: ",argv[0])
    if len(argv) != 2:
        print("Invalid Arguments")
        print("For help type: python   File_Name.py  -h")
        exit()
    if argv[1] == "-h" or argv[1] == "-H":
        print("This application is used to open all the urls from file in browser.")
        print("for usage type: python  File_name.py  -u")
        print("For info: type python filename.py -info")
        exit()
    if argv[1] == "-u" or argv[1] == "-U":
        print("For usage use below command.")
        print("Usage: python  File_name.py  File_Name.extension")
        exit()
    if argv[1] == "-info" or argv[1] == "-INFO":
        print("In this application we open a file and read all the data from the file and find the urls from that file and open all URLS on your default browser.")
        exit()
    if len(argv) == 2:
        Ret = CheckInternetConnection()
        if Ret == False:
            print("There is no Internet connection.")
            print("To see the exact output please connect your computer to the internet.")
            exit()
        else:
            OpenFile(argv[1])

if __name__ == "__main__":
    main()