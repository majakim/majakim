print("Rechne mit mir!")

while True:

    a=float(input("a:"))
    b=float(input("b:"))
    c=input("Addieren?(1), Subtrahieren?(2), Multiplizieren?(3), Dividieren?(4)")

    if c== "1":
        Result=a+b
        
    elif c== "2":
        Result=a-b
        
    elif c== "3":
        Result=a*b

    elif c== "4":
        if b != 0:
            Result=a/b
        else:
            print("Man teilt nicht durch 0")
            continue
    else:
        Result=None
        
    if Result is not None:
        print(Result)
    
    else:
        print("Bitte wählen sie eine der Zahlen 1-4!")

    print("Rechne weiter!")
