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

#print("Data from index 2 is: ",data1[2])

print("Data with UNIQUE elements is:",data)

print("Set is Mutable.")
#Insert data in set

data.add(211)

print("Data after adding data: ",data)

data.remove(211)
print("Data after removal element is: ",data)

data.discard(201) # When element is present in set then this method act like remove method. and if data is not present in Set then it will not generate "KeyError" error.
print("Data after discard element is: ",data)
