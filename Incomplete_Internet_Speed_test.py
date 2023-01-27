import urllib.request
import pyspeedtest

def InterNetBandwidth():
    test = pyspeedtest.SpeedTest("www.youtube.com")

    download = test.download()
    print("Download speed test is: ",download)
    upload = test.upload()
    print("Upload speed test is: ",upload)
    ping = test.ping()
    print("Ping is: ",ping)

def Check_Network():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

def main():
    Bret = Check_Network()
    if Bret == True:
        InterNetBandwidth()
    else:
        print("Please check your network connection.")

if __name__ == "__main__":
    main()
