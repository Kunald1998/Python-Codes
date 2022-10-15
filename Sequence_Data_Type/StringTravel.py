print("Demonstration of string travel.")

String = "Marvellous Infosystems"


print("Print string using for each loop.")
for i in String:
    print(i," ",end="")
print("")


print("Print string using for loop using range() method.")
for i in range(0,len(String),1):
    print(String[i]," ",end="")
print("")


print("Print string in reverse way using for loop.")
for i in range(len(String)-1,-1,-1):
    print(String[i],"",end="")
print("")


print("Print string using while loop.")
i=0
while(i<len(String)):
    print(String[i],"",end="")
    i+=1
print("")