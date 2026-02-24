# WAP for calculate the factorial of a given number by using for  loop 
num = int(input("Enter Number ="))
fact =1
for i in range (1,num+1):
    print(f"{fact}X{i}={fact*i}") 
    fact *=i
print(f"\nFactorial of {num} = {fact}")

