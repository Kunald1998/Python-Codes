print("Example 1")

def addition(*no):
    print(no)
    ans = 0
    for i in no:
        ans = ans + i
    return ans

ret = addition(11,21,51,101) # function call.
print("Addition of given all numbers is: ",ret)

########################################################

print("Example 2")

def Studentinfo(**other):
    print(other)
    for i,j in other.items():
        print(i,j)

Studentinfo(Name="Kunal Deshmane", Age=24, City="Pune", Salary="40000", Company="Marvellous") # function call.


########################################################
print("Example 3")

def StudentInfo(*other):
    print(other)
    for i in other:
        print(i)

StudentInfo("Kunal Deshmane",24,"Pune",40000,"Marvellous") # function call.
######################################################

# Example 1

# (11, 21, 51, 101)
# Addition of given all numbers is:  184

# Example 2

# {'Name': 'Kunal Deshmane', 'Age': 24, 'City': 'Pune', 'Salary': '40000', 'Company': 'Marvellous'}
# Name Kunal Deshmane
# Age 24
# City Pune
# Salary 40000
# Company Marvellous

# Example 3

# ('Kunal Deshmane', 24, 'Pune', 40000, 'Marvellous')
# Kunal Deshmane
# 24
# Pune
# 40000
# Marvellous
#
