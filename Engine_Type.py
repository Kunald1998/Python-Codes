
def Unit_Conversion():
    print("What is your data 'unit'.")
    Unit = input()

    pass
    # Unit conversion is done here.
def Engine_Type_Find(Bore_Dia=1.0,Stroke_len=1.0,No_cylinder=1):
    seperator = "-" * 50
    Swept_vol = 3.14 * ((Bore_Dia / 2)**2) * Stroke_len # Formula to calculate the 'Swept Volume' of cylinder.

    Engine_Displacement = Swept_vol * No_cylinder # Formula to calculate the displacement in cc of your engine.

    Type = (Bore_Dia / Stroke_len)  # Formula to calculate the ratio of Bore dia and Stroke length.
    print(seperator)
    print("Your engine displacement is: {} cc.".format(Engine_Displacement))
    print()
    if(Type > 0.0)and(Type < 1.0):
        print("Your engine is 'Undersquare' engine.")
    elif(Type >= 1.0)and(Type <= 1.9):
        print("Your engine is 'Square' engine.")
    elif(Type >= 2.0):
        print("Your engine is 'Oversquare' engine.")

def main():

    print("Enter 'Bore' diameter in 'cm':",end="")
    Bor_Dia = float(input())

    print("Enter 'stroke' length in 'cm':",end="")
    Str_Len = float(input())

    print("Enter number of cylinder your engine have: ",end="")
    No_Cyl = int(input())

    Engine_Type_Find(Bore_Dia=Bor_Dia,Stroke_len=Str_Len,No_cylinder=No_Cyl)

if __name__ == "__main__":
    main()