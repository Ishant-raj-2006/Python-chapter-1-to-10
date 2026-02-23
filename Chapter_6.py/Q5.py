#WAP to find whether a given username contains less than 10 characters or not
username = str(input("Enter your user name ="))
co = len(username)
if(co<10):
    print("Yes username contains less than 10 characters ")
else:
    print("No username contains less than 10 characters")
