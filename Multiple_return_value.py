def Return():
    no1 = 10
    no2 = 11
    no3 = 12
    return no1,no2,no3 # multiple values can be return in python.


def main():
    value1 = 0
    value2 = 0
    value3 = 0

    value1,value2,value3 = Return(); # Accept multiple return values.

    print(value1)
    print(value2)
    print(value3)

if(__name__ == "__main__"):
    main()