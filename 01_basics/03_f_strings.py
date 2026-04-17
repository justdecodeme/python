# ✨ f-strings: Modern string formatting!
# Similar to JS template literals (`${}`) 🥳

print("...........")
name = "Developer"
greeting = f"Hello, {name}! Welcome to Python. 🐍"
print(greeting)

print("...........")
x = 4
print("x is", x) # x is 4

print("...........")
print("hot", end=' ')
print("dogs", end=' ')
print("taste", end=' ')
print("good") # hot dogs taste good

print("...........")
s1 = "hot"
s2 = "dog"
print(s1, s2) # hot dog
print(s1 + s2) # hotdog
print(s1 + "\t" + s2) # hot     dog
print("hot\tdog")
print(s1 + "\n" + s2) # hot     dog
print("hot\ndog")
print(s1, s2, sep='-') # hot-dog
print(s1, s2, sep='__') # hot__dog

print("...........")
price = 1.35
# >>> Strings and numbers cannot be concatenated 
# print("The price is $" + price) # can only concatenate str (not "float") to str
print("The price is $" + str(price))
