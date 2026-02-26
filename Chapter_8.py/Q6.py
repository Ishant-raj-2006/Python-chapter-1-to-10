# WAP for function which converts inches to cms.

#cm = inches × 2.54
def inch_to_cms(inch):
    cm = inch * 2.54 
    print(cm)
inch = float(input("Enter The value of inch ="))
inch_to_cms(inch)