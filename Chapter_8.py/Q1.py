# WAp for find greatest of three number using function.
def gre():
    a = int(input("Enter 1st numbre = "))
    b = int(input("Enter 2nd number = "))
    c = int(input("Enter 3rd number = "))
    if(a>b and a>c):
        print(f"1st number is greatest {a}")
    elif(b>a and b>c):
        print(f"2nd number is greatest {b}")
    elif(c>a and c>b):
        print(f"3rd number is greatest {c}")
    else:
        print("Sorry ")


gre()