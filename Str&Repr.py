class vehicle:
    model = ""
    price = 0

    def __init__(self,name,value):
        print("Output from Vehicle class.")
        self.model = name
        self.price = value


vobj = vehicle("Dodge",8500000)

print("Object representation in String format using __str__() method is: ",vobj.__str__())
print("Object representation in String format using __repr__() method is: ",vobj.__repr__())

print("Vehicle name is: ",vobj.model)
print("Vehicle price is: ",vobj.price)

"""
OUTPUT:

Output from Vehicle class.
Object representation using __str__() method is:  <__main__.vehicle object at 0x0000021DB4FBBFA0> # Hexadecimal representation.
Object representation using __repr__() method is:  <__main__.vehicle object at 0x0000021DB4FBBFA0> # Hexadecimal representation.
Vehicle name is:  Dodge
Vehicle price is:  8500000
"""

class person:

    Name = ""
    Age = 0

    def __init__(self,string,number):
        print("Output form person class.")
        self.Name = string
        self.Age = number

    def __str__(self):
        print("Output from 'self' method.")
        return f'Person name is {self.Name} and age is {self.Age}.'

    def __repr__(self):
        print("Output from 'repr' method.")
        return f'person name is (name = {self.Name})and age is(age = {self.Age})'
        #return f'Person name is {self.Name} and age is {self.Age}.'


pobj = person("Kunal",24)
"""
As both method return same string represent of object due to this we can call any method by using below 'any' function call. """
print(pobj.__str__()) # using this we can call __str__() method and __repr__() method.
print(pobj.__repr__()) # Using this we can call __repr__() method and __str__() method.
print(pobj) # If any method form str and repr is not written the this method is call to any of the present method from __str__() or __repr__() method.

"""
OUTPUT

Output form person class.
Output from 'str' method.
Person name is Kunal and age is 24.
Output from 'repr' method.
person name is (name = Kunal)and age is(age = 24)
Output from 'str' method.
Person name is Kunal and age is 24.
"""