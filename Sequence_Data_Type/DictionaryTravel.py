print("Demonstration of Dictonary sequence data type.")

# data = Hetrogenous
# Ordered = Yes
# Indexed = No
# Mutable = Yes
# Duplicate = Yes for Value, No for Key

Programming = {"C":"Ritchie","C++":"Strounstupe","Java":"James Gosling","Python":"Rossum"}
Batches = {"PPA":18000,"LB":16700,"Python":16500,"Angular":15000,"LSP":15000}

print("Data of Batches Dictonry is: ",Batches)

print("Data traversal using for-each loop")
for i in Batches:
    print(i)

print("Data traversal using for-each loop using key value and key: ")
for i in Batches:
    print(i,Batches[i])

print("Data traversal using for loop using get method:")
for i in Batches:
    print(i,":",Batches.get(i))


#Below for loop gives error, because dictionary do not have index.
"""for i in range(0,len(Batches),1):
    print("Batches name is: ",keyBatches[i],end = " ")
    print("Fees are: ",ValueBatches[i])"""
