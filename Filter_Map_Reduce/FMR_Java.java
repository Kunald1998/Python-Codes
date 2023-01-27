import java.lang.*;
import java.util.*;

class FMRFunction
{
    public boolean HelperForFilter(int No)
    {
        boolean bret = false;
        if(No % 2 == 0)
        {
            bret = true;
        }
        return bret;
    }
    public int[] FilterX(int Array[],int size)
    {
        int Result[] = new int[size];
        int i,index = 0;

        for(i=0;i<size;i++)
        {
            if(HelperForFilter(Array[i]) == true)
            {
                Result[index] = Array[i];
                index++;
            }
        }
        return Result;
    }

    public int HelperForMap(int No)
    {
        int Ans = No * No;
        return Ans;
    }

    public int[] MapX(int Array[],int size)
    {
        int Result[] = new int[size];
        int i,no = 0;
        for(i=0;i<size;i++)
        {
            no = HelperForMap(Array[i]);
            Result[i] = no;
        }
        return Result;
    }

    public int HelperForReduce(int A,int B)
    {
        int Ans = A + B;
        return Ans;
    }

    public int ReduceX(int Array[])
    {
        int i,Ans = 0;
        int Size = Array.length;
        for(i=0;i<Size;i++)
        {
            Ans = HelperForReduce(Ans,Array[i]);
        }
        return Ans;
    }
}

class FMR
{
    public static void main(String arg[])
    {
        Scanner sobj = new Scanner(System.in);
        FMRFunction fobj = new FMRFunction();
        
        int i = 0;

        System.out.print("Please enter the element that you want to store: ");
        int Size = sobj.nextInt();

        int Data[] = new int[Size];
        int value= 0;
        System.out.print("Please enter the elements:");
        for(i=0;i<Size;i++)
        {
            value = sobj.nextInt();
            Data[i] = value;
        }
        System.out.print("Raw data is: "+"[");
        for(i=0;i<Size;i++)
        {
            System.out.print(" "+Data[i]+" ");
        }
        System.out.print("]");
        System.out.println();

        int Data_From_Filter[] = fobj.FilterX(Data,Size);
        System.out.print("Data after filter is: "+"[");
        for(i=0;i<Size;i++)
        {
            System.out.print(" "+Data_From_Filter[i]+" ");
        }
        System.out.print("]");
        System.out.println();

        int Data_From_Map[] = fobj.MapX(Data_From_Filter,Size);
        System.out.print("Data after Map is: "+"[");

        for(i=0;i<Size;i++)
        {
            System.out.print(" "+Data_From_Map[i]+" ");
        }
        System.out.print("]");
        System.out.println();

        int Data_From_Redduce = fobj.ReduceX(Data_From_Map);
        System.out.print("Data after Reduce is: "+Data_From_Redduce);

    }
}