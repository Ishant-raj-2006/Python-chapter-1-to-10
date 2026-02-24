# WAP to find whether a given number is prime or not.
num = int(input("Enter Number ="))
count = 0
for i in range (1,num+1):
    if(num%i==0):
        count +=1
if(count==2):
    print(f"Yes it is prime number {num}")
else:
    print(f"No it is not prime numebr {num}")