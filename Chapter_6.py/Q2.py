# WAP to find the greatest of four numbres entered by the user.
num1 = int(input("Enter 1st numbre ="))
num2 = int(input("Enter 2nd numbre ="))
num3 = int(input("Enter 3rd numbre ="))
num4 = int(input("Enter 4th numbre ="))
if(num1>num2 and num1>num3 and num1>num4):
    print(f"1st number is greatest {num1}")
elif(num2>num1 and num2>num3 and num2>num4):
    print(f'2nd numbre is greatest {num2}')
elif(num3>num1 and num3>num2 and num3>num4):
    print(f"3rd Number is greatest {num3}")
elif(num4>num1 and num4>num2 and num4>num3):
    print(f"4th number is greatest {num4}")
else:
    print("Somthing Wrong")