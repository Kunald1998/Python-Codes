import pandas as pd
import numpy as np
def MarvellousPandas():
    Data1 = {"One":pd.Series(data=[10,20,30,40,50],index=["a","b","c","d","e"]),"Two":pd.Series(data=[60,70,80,90],index=["f","g","h","i"])}
    Data2 = {"One":pd.Series(data=[101,201,301,401],index=[0,1,2,3]),"Two":pd.Series(data=["Kunal","Anurag","Keshav"],index=[4,5,6])}

    DATA = {"Item1":Data1,"Item2":Data2}

    #pnl = pd.panel(DATA)
    print(pd.__version__)
    print(np.__version__)

    


def main():
    MarvellousPandas()
if __name__ == "__main__":
    main()