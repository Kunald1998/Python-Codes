import pandas as pd
import numpy as np
import openpyxl


# class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
# index = Give the index in the from of list. Usage: provide index for each series line. starts from 0.
# columns = Give the columns names in the from of list. usage: To provide the name to the column.

def MarvellousPandas():
    seperator = 60 * "-"

    print("Creating a empty data frame:")
    df1 = pd.DataFrame()
    print(df1)

    print(seperator)

    lista = [10,20,30,40,50]
    df2 = pd.DataFrame(data=lista,columns=["number"])
    print("Creating the data frame using simple list.")
    print(df2)

    print(seperator)

    listb = [["PPA",4],["LB",5],["Angular"],["Python",4],["LSP",4]]
    df3 = pd.DataFrame(data=listb,index=["a","b","c","d","e"],columns=["Batchs","duration"])
    print("Creating the data frame using list of list with the column names.")
    print(df3)

    print(seperator)

    dictc = {"Batch":["PPA","LB"],"Duration":[3,5]}
    df4 = pd.DataFrame(data=dictc)
    print("Creating the data frame using 'dictionary' with the 'key' value is column names and 'values' value is data of that column.")
    print(df4)

    print(seperator)

    listd = [{"Batch":"PPA","Duration":3,"fees":15000},{"Batch":"LB","Duration":4,"fees":15500},{"Batch":"Angular","Duration":4.5,"fees":14500}]
    #listd = {"Batch":"PPA","Duration":3,"fees":15000}
    df5 = pd.DataFrame(data=listd,index=[0,1,2])
    print(df5)

    dicte = {"One":pd.Series([1,2,3],index=["a","b","c"]),"Two":pd.Series([1,2,3,4],index=["a","b","c","d"])}

    df6 = pd.DataFrame(data=dicte)
    print("---------")
    print(df6["One"])
    print(df6["Two"])
    print(df6)

    datax = {"Number":pd.Series([10,20,30,40,50],dtype=int),"Letters":pd.Series(["A","B","C","D","E"],dtype=str),"Symbols":pd.Series(["!","@","$","%","&"],dtype=str)}

    df1 = pd.DataFrame(datax)
    print("Data frame is: ")
    print(df1)

def MarvellousCreateFile():
    """
    Data = [{"Batch":"PPA","Duration":4,"Fees":15000},{"Batch":"LB","Duration":3.5,"Fees":14000},{"Batch":"Angular","Fees":14500},{"Batch":"Python","Duration":4,"Fees":16500}]
    
    df = pd.DataFrame(Data)
    print(df)
    Writer = pd.ExcelWriter(path="MarvellousInfo.xlsx",engine="xlsxwriter")
    df.to_excel(excel_writer=Writer,sheet_name="Piyush")
    Writer.save()
    #----------------------------------------------
    pathx = "Marvellous.xlsx"

    batches = pd.read_excel(pathx)
    
    print(batches.head())
    print(batches.head(2))
    print("last 5 entries are: ")
    print(batches.tail())
    print("last 3 entries are: ")
    print(batches.tail(3))
    #----------------------------------------------
    """
    pathx = "Marvellous.xlsx"

    reader = pd.read_excel(pathx,sheet_name=0,index_col=0)
    print(reader.head())

    print()
    print()

    xlsx = pd.ExcelFile(pathx)

    batches_sheets = []
    
    for sheet in xlsx.sheet_names:
        print(sheet)
        batches_sheets.append(xlsx.parse(sheet))
    
    batche = pd.concat(batches_sheets)
    print(batche)

def Create_xlsx_File():
    import xlsxwriter
    name = input("Enter the name of file: ")

    workbook = xlsxwriter.Workbook(name)

    worksheet = workbook.add_worksheet()

    worksheet.write("A1","Name")
    worksheet.write("B1","Age")
    worksheet.write("C1","City")
    worksheet.write("D1","gender")
    worksheet.write("E1","salary")
    
    workbook.close()

def main():
    Create_xlsx_File()

if __name__ == "__main__":
    main()