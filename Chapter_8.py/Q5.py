# WAP for print star ulta trangel .
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
num = int(input("Enter number ="))
pattern(num)