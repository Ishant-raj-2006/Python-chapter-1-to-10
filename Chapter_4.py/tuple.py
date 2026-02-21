a = (1,2,3,4,5,False,"Ishant","Raj",5)
print(type(a))
print(a)

# tuple me find kro ki ko sa element kitna time aa raha h '.count(jise find krna h kitne times aaya h )' function ka use karte h 
no = a.count(5)
print(no)

#tuple me kisi bhi elemrnt ka index number find krna hoga toh '.index(element)' function ka use karte h 
index = a.index(5)
print(index)


# find tuple length 
print(len(a))