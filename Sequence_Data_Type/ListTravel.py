Data = [11,21,51,101]
Data1 = [10,"Hello",3.145,True,15]

print("Output using for-each loop:")

for no in Data: # This loop is like for each loop.
    print(no,end=" ")
print("")

print("Output using for loop with index:")

for i in range(0,len(Data),1):
    print(Data[i],end=" ")
print("")

print("Output using while loop: ")
i = 0
while(i < len(Data)):
    print(Data[i],end = " ")
    i+=1
print("")

print("Data from Data1 is:")
for i in range(0,len(Data1)):
    print("|",i,"|","=>",Data1[i],end=" ")
print("")

print("List travel in reverse direction using range method in for loop.")
for j in range(len(Data)-1,-1,-1):
    print(Data[j],end=" ")
print("")

print("List travel in reverse direction using reversed() method in for-each loop.")

for k in reversed(range(0,len(Data),1)):
    print(Data[k],end=" ")
print("")