print("Demonstration of Dictonary sequence data type.")

# data = Hetrogenous
# Ordered = Yes
# Indexed = No
# Mutable = Yes
# Duplicate = Yes for Value, No for Key

Programming = {"C":"Ritchie","C++":"Strounstupe","Java":"James Gosling","C":" ","Python":"Rossum","C":"Thompson"}
Batches = {"PPA":18000,"LB":16700,"Python":16500,"Angular":15000,"LSP":15000}

print("Data from Batches Dictonary: ",Batches)
print("Data from programming Dictonary is: ",Programming)
print("Data type is: ",type(Batches))
print("Length of Batches Dictonary is: ",len(Batches))
print("Value of PPA is: ",Batches["PPA"])
print("Value of C++ is: ",Programming["C++"])

print("insert data using dictionary_name[Key_name] = New_value is:")
Batches["PPA"] = 19000
print(Batches)

Programming["Python"] = "Gudo van Rossum"
print(Programming)

keyBatches = Batches.keys() # Due to this we get only keys.
print(keyBatches)
print("Type of key is: ",type(keyBatches))

ValueBatches = Batches.values() #Due to this we get all Values.
print(ValueBatches)
print("Type of values is: ",type(ValueBatches))

"""
OUTPUT
Demonstration of Dictonary sequence data type.
Data from Batches Dictonary:  {'PPA': 18000, 'LB': 16700, 'Python': 16500, 'Angular': 15000, 'LSP': 15000}
Data from programming Dictonary is:  {'C': 'Thompson', 'C++': 'Strounstupe', 'Java': 'James Gosling', 'Python': 'Rossum'}
Data type is:  <class 'dict'>
Length of Batches Dictonary is:  5
Value of PPA is:  18000
Value of C++ is:  Strounstupe
insert data using dictionary_name[Key_name] = New_value is:
{'PPA': 19000, 'LB': 16700, 'Python': 16500, 'Angular': 15000, 'LSP': 15000}
{'C': 'Thompson', 'C++': 'Strounstupe', 'Java': 'James Gosling', 'Python': 'Gudo van Rossum'}

"""


