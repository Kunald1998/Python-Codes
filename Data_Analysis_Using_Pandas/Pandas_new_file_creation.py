"""
import csv
def demo():
    data = pd.read_csv(FileName,usecols=["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age","Outcome"])

    NewFile = "New.csv"

    fd = open(file=NewFile,mode="w")

    listx = data.columns

    csv_obj = csv.DictWriter(fd,listx)

    csv_obj.writeheader()

    last = len(data["Pregnancies"])
    

    for i in range(0,last):
        csv_obj.writerow(data[listx[i]].values)



   
    #print("Data is: ",data)
    newData = dict(data)
    print("new data is: ",newData)

    open(file="New.csv",mode="w")

    df = pd.read_csv("New.csv")

    df.to_csv(newData)
"""