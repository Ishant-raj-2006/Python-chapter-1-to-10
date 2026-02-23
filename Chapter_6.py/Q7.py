# WAP to calculate the grade of a student from his marks from the following scheme:
# 90 - 100 ==> Ex
# 80 - 90 ==> A
# 70 - 80 ==> B
# 60 - 70 ==> C
#50 - 60 ==> D 
# <50    ==> F
marks = float(input("Enter your marks = "))

if 90 <= marks <= 100:   
    print("Ex")
elif 80 <= marks < 90:
    print("A")
elif 70 <= marks < 80:
    print("B")
elif 60 <= marks < 70:
    print("C")
elif 50 <= marks < 60:
    print("D")
else:
    print("F")
