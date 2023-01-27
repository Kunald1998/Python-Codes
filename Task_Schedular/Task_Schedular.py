import schedule
import datetime
import time

def Fun_Minute():
    print("Inside Fun_Minute.")
    print("Current time is: ",datetime.datetime.now())
    print("Schedular executes after a MINUTE.")

def Fun_Hour():
    print("Inside Fun_Hour.")
    print("Current time is: ", datetime.datetime.now())
    print("Schedular executes after an HOUR.")

def Fun_Day():
    print("Inside Fun_Day.")
    print("Current time is: ", datetime.datetime.now())
    print("Schedular executes after a DAY.")

def Fun_Afternoon():
    print("Inside Fun_Afternoon.")
    print("Current time is: ", datetime.datetime.now())
    print("Schedular executes after at 12 PM.")

def main():
    print("Marvellous Infosystems By Piyush Manohar Khairnar.")
    print("Current time is: ",datetime.datetime.now())
    print("The script is running....")

    schedule.every(5).minutes.do(Fun_Minute)

    schedule.every().hour.do(Fun_Hour)

    schedule.every().sunday.do(Fun_Day)

    schedule.every().sunday.at("06:00").do(Fun_Afternoon)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()