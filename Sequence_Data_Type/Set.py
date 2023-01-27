print("Demonstration of Set sequence data type.")

# data = Hetrogenous
# Ordered = No
# Indexed = No
# Mutable = Yes
# Duplicate = No

data = {11,21,51,101,11,21,151,121} # Duplicate
data1 = {11,90.12,True,"Hello"} #Hetrogenous

print("First set data is: ",data)
print("Length of data is: ",len(data))
print("Data type of data1 is: ",type(data1))
print("Dat is Hetrogenous:",data1)
print("Data is unordered: ",data1)

#print("Data from index 2 is: ",data1[2]) No index is available for set.
# Subcriptable error means you cant write any thing inside the [].

print("Data with UNIQUE elements is:",data)

print("Set is Mutable.")
print("Length of data is: ",len(data))

#Insert data in set

data.add(211)
print("Data after adding data: ",data)

data.remove(211) # if the data is present in the set then it will remove that value and if that data is not present in that list then PVM generate 'Keyerror'.
print("Data after removal element is: ",data)

data.discard(201) # When element is present in set then this method act like remove method. and if data is not present in Set then it will NOT generate "KeyError" error.
print("Data after discard element is: ",data)

"""
OUTPUT

Demonstration of Set sequence data type.
First set data is:  {51, 101, 21, 151, 121, 11}
Length of data is:  6
Data type of data1 is:  <class 'set'>
Dat is Hetrogenous: {True, 90.12, 11, 'Hello'}
Data is unordered:  {True, 90.12, 11, 'Hello'}
Data with UNIQUE elements is: {51, 101, 21, 151, 121, 11}
Set is Mutable.
Length of data is:  6
Data after adding data:  {51, 211, 101, 21, 151, 121, 11}
Data after removal element is:  {51, 101, 21, 151, 121, 11}
Data after discard element is:  {51, 101, 21, 151, 121, 11}

"""