# A span comment is defined as a text containg following keywords:
# "make a lot of moeny", "Buy now", "Subscribe this ", "click this ", write a program to detect these spams.
 
p1 = "make a lot of moeny"
p2 ="Buy now"
p3 = "Subscribe this"
p4 = "click this"
message = input("Enter your comment:")
if((p1 in  message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam ")
else:
    print("this comment is not spam ")