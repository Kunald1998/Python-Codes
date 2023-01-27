#include<iostream>
using namespace std;

int HelperForFilter(int No)
{
    if(No % 2 == 0)
    {
        return true;
    }
    else
    {
        return false;
    } 
}

int * FilterX(int Array[],int size,int * ptr)
{
    int * Result = new int[size];
    
    int i,index = 0;
    for(i=0;i<size;i++)
    {
        if(HelperForFilter(Array[i]) == true)
        {
            Result[index] = Array[i];
            index++;
        }
    }
    *ptr = index;
    return Result;
}

int HelperForMap(int No)
{
    int iMult = 0;
    iMult = No * No;
    return iMult;
}

int * MapX(int Array[],int size)
{
    int * Result = new int[size];
    int i = 0;
    for(i=0;i<size;i++)
    {
        Result[i] = HelperForMap(Array[i]);
    }
    return Result;
}

int HelperForReduce(int A,int B)
{
    int Ans = 0;
    Ans = A + B;
    return Ans;
}

int ReduceX(int Array[],int size)
{
    int i,Sum = 0;
    for(i=0;i<size;i++)
    {
        Sum = HelperForReduce(Sum,Array[i]);
    }
    return Sum;
}

int main()
{
    int index = 0;
    int i = 0;
    int size = 0;

    cout<<"Enter the element that you want to store: ";
    cin>>size;

    int * Data = new int[size];
    cout<<"Enter the elements: ";
    for(i=0;i<size;i++)
    {
        cin>>Data[i];
    }
    
    int * Data_Output_Filter = FilterX(Data,10,&index); 
    // Above Here &index is used bcoz we wnat return value for that we change the value of index variable value using call by address method.
    
    int Data_From_Filter[index];
    for(i=0;i<index;i++)
    {
        Data_From_Filter[i] = Data_Output_Filter[i];
    }
    cout<<"Data from the Filter is: ";
    for(i=0;i<index;i++)
    {
        cout<<" "<<Data_From_Filter[i];
    }
    cout<<"\n";

    int * Data_Output_Map = MapX(Data_From_Filter,index);
    int Data_From_Map[index];
    for(i=0;i<index;i++)
    {
        Data_From_Map[i] = Data_Output_Map[i];
    }
    cout<<"Data from the Map is: ";
    for(i=0;i<index;i++)
    {
        cout<<" "<<Data_From_Map[i];
    }
    cout<<"\n";

    int Data_Output_Reduce = ReduceX(Data_From_Map,index);

    cout<<"Data after reduce is: "<<Data_Output_Reduce;
    
 return 0;
}