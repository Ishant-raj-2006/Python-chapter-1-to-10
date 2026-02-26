# WAP for print multiplication for table of a given number using function.
def table(num):
    for i in range(1,11,1):
        print(f"{num}X{i}={num*i}")
num = int(input("Enter Number = "))
table(num)