# ⚡ Lambda Functions: Anonymous "one-liners"
# Similar to Arrow Functions in JavaScript: (x, y) => x * y

print("--- Testing Lambdas ---")

# ❌ The "Anti-Pattern" (Ruff E731)
# Why the warning? PEP 8 recommends using 'def' for named functions.
# Assigning a lambda to a variable defeats its purpose of being "anonymous"
# and makes stack traces harder to debug.
multiply = lambda x, y: x * y

# def multiply(x, y):
#     return x * y

print(f"3 x 4 = {multiply(3, 4)} 🧮")


# ✅ The "Pythonic" Use Case: Inline Logic
# Lambdas shine when passed as arguments to other functions like sorted(), map(), or filter().
# They stay anonymous and don't clutter the namespace with a function name used only once.

users = [{"name": "Rakesh", "id": 2}, {"name": "Kiran", "id": 1}]

# Using lambda as a 'key' to tell sorted() which property to compare
# This is where lambdas are perfectly acceptable and standard.
sorted_users = sorted(users, key=lambda user: user["id"])

print(f"Sorted Users: {sorted_users}")
