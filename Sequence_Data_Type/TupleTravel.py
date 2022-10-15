print("Demonstration of tuple sequence data type.")

# data = Hetrogenous
# Ordered = Yes
# Indexed = Yes
# Mutable = No
# Duplicate = Yes

data = (11,21,51,101,11)
data1 = (11,90.12,True,"Hello") #Hetrogenous

print("Display tuple using for loop.")

for i in range(0,len(data),1):
    print(data[i],end=" ")
print("")
print("Display tuple using while loop.")
i = 0
while(i < len(data)):
    print(data[i],end="")
    i = i+1
print("\n")

print("Display tuple using for loop and reversed() method in reverse order.")

for j in reversed(range(0,len(data1),1)):
    print(data1[j],end=" ")
print("")

print("Display tuple using for loop in reverse order.")
for k in range(len(data1)-1,-1,-1):
    print(data1[k],end=" ")
print("")

"""
OUTPUT
Demonstration of tuple sequence data type.
Display tuple using for loop.
11 21 51 101 11
Display tuple using while loop.
11215110111

Display tuple using for loop and reversed() method in reverse order.
Hello True 90.12 11
Display tuple using for loop in reverse order.
Hello True 90.12 11

"""
