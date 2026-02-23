# WAP to find out whether a student a has paased or failed  if it requrires a total of 40%
# and at lest 33% in each subject to pass . Assume 3 subject and take marks as an input from user 

sub1 = float(input("Enter Your marks of sub1 ="))
sub2 = float(input("Enter Your marks of sub2 ="))
sub3 = float(input("Enter Your marks of sub3 ="))
if(sub1<33 or sub2<33 or sub3<33):
    print("Sorry you are fail")
elif((sub1+sub2+sub3)/3>40):
    print(f"You are pass with sub1 marks is {sub1} sub2  marks is {sub2} sub3 marks is {sub3} \n = total marks is  {sub1+sub2+sub3}  and persentage is {(sub1+sub2+sub3)/3}")
else:
    print("Somthing worng try angrin later ")