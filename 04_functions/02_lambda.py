# ⚡ Lambda: Anonymous functions (Arrow functions in JS)
# Short, one-line functions! ✍️

print("...........")

# def multiply(x, y):
#     return x * y

# It's throwing warning because....
multiply = lambda x, y: x * y

print(f"3 x 4 = {multiply(3, 4)} 🧮")

users = [{"name": "Rakesh", "id": 2}, {"name": "Kiran", "id": 1}]

# Here, the lambda is perfect because it doesn't need a name
sorted_users = sorted(users, key=lambda user: user["id"])
print(sorted_users)
