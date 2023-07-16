word = input("Enter any string\n")
new_word = ""

# Using loop
for i in word:
    new_word = i + new_word
print(new_word)

# using slicing
print(word[::-1])

# using reversed()
word = "".join(reversed(word))
print(word)
