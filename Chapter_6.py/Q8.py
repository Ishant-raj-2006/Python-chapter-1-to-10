# WAP to find out wethr a give post is talking about "Ishant " or not 
post = input("Enter the post = ")
if("Ishant".lower() in post.lower() ):
    print("This post taking about Ishant ")
else:
    print("This post Not taking about Ishant ")