while True:
    try:
        x = int(input("Please enter an integer: "))
        a,b=0,1
        while b<x:
            print(b)
            a,b=b,a+b
        print("Complete")
        break
    except ValueError:
            print("Oops...Only number's accepted")