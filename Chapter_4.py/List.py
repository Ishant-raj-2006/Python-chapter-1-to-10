List = ["Hello","Ishant","Raj",8317735828,845437]
print(List[3])
List[3] = 9576 # unlike Strings list are mutable
print(List[3])
print(List[0:4+1])
List.append("shrivastav") # iska matlab ki jo bhi mera list h append function ke under jo bhi likho toh wo list ke end me chipka dega 
print(List)

# List ko sort karne ka function 'short' ye ek varival name h '.sort' function h 
short = [1,35,16,78,15]
short.sort()
print(short)

# List ko reverse karne ke liye '.reverse' function ka use kiya jata h 
short.reverse()
print(short)

# List me kisi particular index pe kisi bhi chiz ko store krne ke liye '.insert(index number, element)' function ka use krte h 
short.insert(2,845437)
print(short)

# List me se kisi particular index ki element ko delet krna ho toh '.pop(index Number) ' function ka use krte h 
print(short.pop(2))
print(short)

# List me se kisi particular index ki element ko remove krna ho toh '.remove(element) ' function ka use krte h
short.remove(1)
print(short)

# 