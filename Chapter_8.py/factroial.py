# WAP program for print factrial of any number .
def fact(n):
    i = n 
    if(n==1 or n==0):
        return 1
    print(f"{n}X{i-1} = {n*(i-1)}")
    return n*fact(n-1)
    i -=i


n= int(input("Enter Number = "))
print(f"the factorial of this {n}  number = {fact(n)}")



# WAP program to print factorials line-by-line for every number from 1..n



def print_factorial_lines(n):
    if n < 0:
        print("Please enter a non-negative integer.")
        return

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        if i == 1:
            terms = "1*1"       
        else:
            terms = "*".join(str(j) for j in range(i, 0, -1))
        print(f"{i}={terms}={factorial}")


if __name__ == "__main__":
    try:
        s = input("Enter Number = ").strip()
        n = int(s)
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        print_factorial_lines(n)