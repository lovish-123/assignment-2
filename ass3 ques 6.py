a = int(input("enter the first side : "))
b = int(input("enter the second side : "))
c = int(input("enter the third side : "))
if (a+b>=c and a+c>=b and b+c>=a):
    print("yes, it can form a triangle")
else:
    print("no, it cannot form a triangle")