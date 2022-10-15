print("Demonstration of tuple sequence data type.")

# data = Hetrogenous
# Ordered = Yes
# Indexed = Yes
# Mutable = No # It is like constant array.
# Duplicate = Yes

data = (11,21,51,101,11,21)
data1 = (11,90.12,True,"Hello") #Hetrogenous


print("Data type of data1 is: ",type(data1))
print("Data is Hetrogenous:",data1)
print("Data is orderes is: ",data1)
print("Access data using index.","Data from index 3 is: ",data1[3])
print("Data with duplicate elements is:",data)

# we can only concat tuple to tuple not tuple to any other data type.

print("Concatination of two tuples together.")
Tuple = data + data1
print("After concatenation of two tuples: ",Tuple)


# List = ["%","^","*","@","$"]
List = list(data)
print("Converting tuple to list: ",List)
print(type(List))
List.insert(3,75)
print("after insert data into list at index no 3 is:",List)

Tuple1 = tuple(List)

print("After concersion of list to tuple is: ",Tuple1)


"""
OUTPUT
Demonstration of tuple sequence data type.
Data type of data1 is:  <class 'tuple'>
Data is Hetrogenous: (11, 90.12, True, 'Hello')
Data is orderes is:  (11, 90.12, True, 'Hello')
Access data using index. Data from index 3 is:  Hello
Data with duplicate elements is: (11, 21, 51, 101, 11, 21)
Concatination of two tuples together.
After concatenation of two tuples:  (11, 21, 51, 101, 11, 21, 11, 90.12, True, 'Hello')
Converting tuple to list:  [11, 21, 51, 101, 11, 21]
<class 'list'>
after insert data into list at index no 3 is: [11, 21, 51, 75, 101, 11, 21]
After concersion of list to tuple is:  (11, 21, 51, 75, 101, 11, 21)
"""
