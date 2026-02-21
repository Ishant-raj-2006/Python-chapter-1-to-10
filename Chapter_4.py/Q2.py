# WAP to accept marks of 6 students and display them in a sored manner.
num = int(input("Enter the number of stdents ="))
marks =[]
for i in range(1 , num+1):
    m = int(input(f"Enter the marks of {i} student ="))
    marks.append(m)
marks.sort()
print(marks)