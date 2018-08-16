print("Enter 1 number")
a=int(input())
print("enter 2nd no")
b=int(input())
print("press 1 for add 2 for sub 3 for mul and 4 for div")
s=int(input())
if s==1:
    print("so you want to perform addition on numbers %d & %d"+a +b)
    add=a+b
    print("sum of numbers is "+add)
elif s==2:
    print("so you want to perform subtraction on numbers %d & %d"+a +b)
    sub==a-b
    print("subtraction of numbers is "+sub)
elif s==3:
    print("so you want to perform multiplication on numbers %d & %d"+a +b)
    m=a*b
    print("multiplication of numbers is "+m)
elif s==4:
    print("so you want to perform division on numbers %d & %d"+a +b)
    div=a/b
    print("division of numbers is "+div)
else:
    print("you've entered an incorrect option, read it again")
