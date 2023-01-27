import pandas as pd
import numpy as np
print("This code is used to demonstrates of creation of the'Series' using the pandas library.")
# class pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

def MarvellousPandas():
    print("Creating an Empty series: ")
    sr1 = pd.Series(dtype=float)
    print(sr1)

    print()
    
    listx = [10,20,30,40,50,60]
    dictx = {"PPA":15000,"LB":14500,"Angular":15600,"Python":16500}
    tuplex = ("A","B","C","D")
    Str = "Marvellous"
    setx = {"K","U","N","A","L"}

    Data = np.array(listx) # Converting list into array using numpy library.
    sr2 = pd.Series(data=Data,dtype=int,name="Kunal")
    print("Creating Series from array is: ")
    print(sr2)
    print("Access the indexed element: ",sr2[2])# output = 30

    print()
    
    sr3 = pd.Series(listx)
    print("Creating series form list is: ")
    print(sr3)

    print()
    
    sr4 = pd.Series(dictx)
    print("Creating a series from dictionary: ")
    print(sr4)
    
    print()

    sr5 = pd.Series(tuplex)
    print("Creating a series from tuple: ")
    print(sr5)

    print("We can not create a series using set sequence data type because data is not ordered.")

    """
    We can not create a series using set sequence data type because data is not ordered.
    sr12 = pd.Series(setx)
    print("Creating series using set data type.")
    print(sr12)
    """
    print()

    Data = np.array(Str)
    sr6 = pd.Series(Data)
    print("Creating a series from string: ")
    print(sr6)
    
    print()
    
    sr7 = pd.Series(Str, index=["A","B","C","D","E","F"])
    print("We can provide index for the data.")
    print(sr7)

    print()

    print("Create the series in the form of range method.")
    sr8 = pd.Series(np.linspace(start=3,stop=33,num=3,endpoint=True,retstep=False,dtype=None, axis=0)) # or np.linspace(3,33,3)
    print(sr8)
    
    print()
    
    sr9 = pd.Series(np.linspace(1, 100, 10)) # Same as above.
    print(sr9)

    print()

    sr10 =pd.Series(range(10)) # Creating series from 0 to 9 same like a range method from for loop.
    print("Creating series using range method:")
    print(sr10)

    print()

    sr11=pd.Series(range(1,20,3), index=[x for x in 'abcdefg'])
    print("Creating series using range method by providing the all three parameters.")
    print(sr11)


def main():
    MarvellousPandas()

if __name__ == "__main__":
    main()