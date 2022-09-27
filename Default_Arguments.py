print("Demonstration of default parameters for functions.")

def AreaOfCircle(radius, pi = 3.14): # Here "pi" is a default parameter.
    Area = pi * radius*radius
    return Area

def main():
    ret = 0

    ret = AreaOfCircle(10,11)       # Here we provide value for "pi" variabe.
    print("Area with both parameters: ",ret)

    ret = AreaOfCircle(10)      # Here we NOT provide value for "pi" variabe.
    print("Area with only one parameter: ", ret)

if __name__=="__main__":
    main()
