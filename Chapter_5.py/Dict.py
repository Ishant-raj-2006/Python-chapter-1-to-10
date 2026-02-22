# Find marks 
marks={
    "Ishant" : 100,
    "Raj" : 95,
    "Srivastav" : 90,
    "Rohan" : 85
}
print(type(marks))
print(marks["Ishant"])




# PROPERTIES OF PYTHON DICTIONARIES
# 1. It's unordered.
# 2. it's Mutable.
# 3. it's Indexed.
# 4. Cannot contain duplicate keys.



# Methods of dictionary 
# 1. 'marks.items()' return a list of (key,value)tuples.
print(marks.items())


# 2. 'marks.keys()' , return keys that means right side values
print(marks.keys())

# 3. 'marks.values()' Return values that means left side values 
print(marks.values())

# 4. 'marks.upate({"value":keys})' just like I want to update the marks of ishant with 80.
marks.update({"Ishant":80})
print(marks)

# 4a. 'marks.update({"Valus":keys})' isse discinary me kuchh add bhi kr sakte h 
marks.update({"Renuka":87})
print(marks)

# 5. 'marks.get("values")' , when which values we enterd if not exit in the disc then reurn null
print(marks.get("raju"))

# 5a. 'print(marks["Ishant"])' ,  when which values we enterd if not exit in the disc then reurn error

# print(marks["raju"])
 

