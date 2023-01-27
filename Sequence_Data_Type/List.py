print("Demonstration of list sequence data type.")

# PROPERTIES OF LIST DATA TYPE.
# data = Heterogeneous
# Ordered = Yes
# Indexed = Yes
# Mutable = Yes {We can overwrite the element from a particular index.}
# Duplicate = Yes

data = [11,21,51,101,11]

data1 = [11,90.12,True,"Hello"] # Heterogeneous

Batch = ["PPA","LB","Angular","Python"]

print("Data type of Data is:",type(data))
print("Data is Heterogeneous:",data1)
print("Data is ordered: ",data1)
print("Data from index 1 is: ",data1[1])
print("Data with duplicate elements is:",data)
data[0] = "IN" # we replace 0th index element with string "IN" this proves list is mutable.
print("Data is mutable: ",data)

# Different methods from list data type.
data1.append(100)
print(data1)

data.append(121)
print(data)

data.remove(51)
print(data)

data1.pop() # if we use pop() method then last element of list gets removed.
print(data1)

data.pop(1) # 1 is the index number. We can remove the element using by providing the index to the pop method.
# If we not provide index then pop method remove the last element or list index element of that list.
print("Data pop from index 1st is:",data)

data1.insert(2,"Kunal") # Here index get shifted.
print(data1)

data.insert(-2,"KD")
print(data)

data.insert(-1,"AD")  # When you give index for the insert() function in negative format then that element is insert from back side of that list at that negative index.
print(data)

# We can ctrate list of list.
combine = [data + data1] # OR combine = [data,data1]
print("List after combining is:",combine)


Batch.extend(["LSP","MultiOS","WindowsProgramming"]) # Here we add or joint another list on privious list.

Batch.sort() # By using sort() method we can sort the list element in alphabetical order.

print("List after sort is: ",Batch)

del Batch[2:] # Here we remove all the elements from 1 to till the end.
print("After deleting element from 2nd index to last is: ",Batch)

#del Batch[:2] # Here we remove/delete all the element from 2nd index to first index ie. 0th index.

# "":index" This represent we delete all the element of Left side of the index including the index also.
# "index:"" This represent we delete all the element of Right side of the index including the index also.

"""
OUTPUT
Demonstration of list sequence data type.
Data type of Data is: <class 'list'>
Data is Heterogeneous: [11, 90.12, True, 'Hello']
Data is ordered:  [11, 90.12, True, 'Hello']
Data from index 2 is:  90.12
Data with duplicate elements is: [11, 21, 51, 101, 11]
Data is mutable:  ['IN', 21, 51, 101, 11]
[11, 90.12, True, 'Hello', 100]
['IN', 21, 51, 101, 11, 121]
['IN', 21, 101, 11, 121]
[11, 90.12, True, 'Hello']
Data pop from index 1st is: ['IN', 101, 11, 121]
[11, 90.12, 'Kunal', True, 'Hello']
   0    1     2   3   4
['IN', 101, 'KD', 11, 121]
 -4    -3    -2   -1   0
  0     1     2    3   4     5
['IN', 101, 'KD', 11, 'AD', 121]
  -5   -4    -3    -2   -1   0
List after combining is: [['IN', 101, 'KD', 11, 'AD', 121, 11, 90.12, 'Kunal', True, 'Hello']]
List after sort is:  ['Angular', 'LB', 'LSP', 'MultiOS', 'PPA', 'Python', 'WindowsProgramming']
Delete element from 1st index to last is:  ['Angular']


 0   1    2    3    4    5    6   = index
[11, 21, 101, 'KD', 11, 'AD', 121]
-6   -5  -4    -3   -2   -1    0   = index
"""