import pandas as pd
import csv
import numpy as np

def Marvellous(FileName):
    df = pd.read_csv(FileName)

    #mean = np.mean(df["Pregnancies"].values)

    #df.dropna(subset=["Pregnancies"],axis=0,inplace=True)
    mean = df["Pregnancies"].mean()

    df["Pregnancies"].replace(np.nan,mean)
    print(df)

    #print(df["Pregnancies"].head())

    #df["Pregnancies"].replace("NaN",)


def DataNormalization(FileName):
    df = pd.read_csv(FileName)

    # If data contains large values like 100000 then convert this 
    # values into small values like from 0 to 1.
    # to convert that values use below formula.
    # x_new = x_old / x_Max
    # x_max = maximum value from that column.
    # x_old = old value which is replaced with x_new value.

    # eg.syntax=  df["length"] = df["length"] / df["length"].max()

def Binning():
    # If any column like "Price" contains values which are
    # in the form of group eg. 10-20, 100-1000 like that then
    # provide that range a catagorical value
    # like eg. for 10-20 we provide "Low" name
    # for 100-1000 we give "Medium" and for 1000-1000000 we give "High" catagory.
    # Syntax = bins = numpy.linespace(min(df["price"]),max(df["price"]),4)
    pass

def Catagorcal_variables():
    pass
    # One hot encoding.


def main():
    filename = "Actual.csv"
    Marvellous(filename)

if __name__ == "__main__":
    main()