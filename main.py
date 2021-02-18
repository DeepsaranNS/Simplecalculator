def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("**************CALCULATOR**************")
print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. All Operations""")
choice = (float(input("Enter the choice to perform:")))
n = [1,2,3,4,5]
if choice in n:
    pass
else:
    print("please choose from the given option")
    exit(0)
a =(int(input("enter the 1st number")))
b =(int(input("enter the 2nd number")))

if choice==1:
    print("addition of the 2 numbers is:")
    print(add(a,b))

elif choice==2:
    print("subtraction of the 2 numbers is:")
    print(sub(a,b))

elif choice==3:
    print("multiplication of the 2 numbers is:")
    print(mul(a,b))

elif choice ==4:
    print("division of the 2 numbers is:")
    print(div(a,b))

else:
    print("Addition = %s" % add(a,b))
    print("Subtraction = %s" % sub(a,b))
    print("Multiplication = %s" % mul(a,b))
    print("Division = %s" % div(a,b))

