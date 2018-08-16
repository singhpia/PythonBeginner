#print("enter any number")
#a=int(input())
#a=a+3
#print("value of a is",+a)
#if a<10:
#    print("you're correct")
#else:
#    print("value is not greater than 10")

print("enter two digit number")
a=int(input())
print("enter one more two digit number")
b=int(input())
unitd=int(b%10)
prod1=a*unitd
tensd=int(b/10)
prod2=*(tensd*10)
result=prod1+prod2
print("the product of two numbers is {0}".format(result))
