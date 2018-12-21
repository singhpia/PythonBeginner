#takes input from user
print("enter two digit number")
a=int(input())
print("enter one more two digit number")
b=int(input())
#finding the unit digit of second number
unitdigit=int(b%10)
#multiply unit digit number by first number
prod1=a*unitdigit
#finding tens digit of second number
tensdigit=int(b/10)
#multiply tens digit by first number
prod2=(tensdigit*10)
#the result will be the sum of these products
result=prod1+prod2
print("the product of two numbers is {0}".format(result))
