n1 = input("enter the first number :")
n2 = input("enter the second number :")
n3 = input("enter the third number :")
if n1>n2:
    if n1>n3:
        print("n1 is the greatest number")
    else:
        print("n3 is the greatest number")
elif n2>n3:
    print("n2 is the greatest number")
else:
    print("n3 is the greatest numnber")