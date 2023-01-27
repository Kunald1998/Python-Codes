def Add(a,b):
    return a+b

def Sub(a,b):
    return (a-b) 

def Multi(a,b):
    return a*b

def Division(a,b):
    if b == 0:
        raise ValueError("Cant divide by zero.")
    return a/b