a = "I am Priya and I\'m from Lucknow"
#string slicing using range
print(a)
print(a[3:12])
print(a[-4])

#validating if substring is present in string
print('Priya' in a)
print("car" not in a)

#string built in methods

#to get the index of a character present in a string
print('python'.index('n'))
print("manipulation".index('o'))

#length of string
print(len("manipulation"))
print(len(a))

s = 'car'
#changing the case
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.replace('m', '@'))

print(a)
#split
print(a.split("and"))
str1, str2 = a.split("and")
print(str1,str2)
print(len(str1))
print(type(str1))
print(str1.replace(" ",""))


#join
pest = "\'".join(a)
print(pest)
print("*".join(a))
print("*".join("priyaaa"))

#trim whitespaces using strip
z = "      hey!! !!!!!  "
print(z.strip())
print(z.lstrip())
print(z.rstrip())

#reverse a string
print("".join(reversed(a)))
print("".join(list(a)[::-1]))

#text alignment
print(a.rjust(40))
print(a.ljust(100))
print(a.center(70))
print(a.rjust(90, '*'))