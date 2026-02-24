# WAP to find sum of n natural number using while loop.
num = int(input("Enter number ="))
i=1
sum =0
while(i<=num):
    sum += i
    i +=1
print(f"The sum of 1 to {num} natural number = {sum} ")