# 📝 1. LIST COMPREHENSION
# Goal: Create a list of squares for even numbers only.

numbers = [1, 2, 3, 4, 5, 6]

# Syntax: [expression for item in iterable if condition]
squares = [n**2 for n in numbers if n % 2 == 0]

print(f"Even Squares: {squares} ✅")  # [4, 16, 36]


# 💎 2. SET COMPREHENSION
# Goal: Extract unique first letters from a list of names.
# Remember: Sets automatically handle deduplication!

staff = ["Amit", "Zara", "Ankit", "Zara", "Raj"]

# Syntax: {expression for item in iterable}
initials = {name[0] for name in staff}

print(f"Unique Initials: {initials} ✨")  # {'A', 'Z', 'R'}


# 📖 3. DICTIONARY COMPREHENSION
# Goal: Create a map of names to their character lengths.

devs = ["Rakesh", "Kiran"]

# Syntax: {key_expr: value_expr for item in iterable}
dev_map = {name: len(name) for name in devs}

print(f"Developer Name Lengths: {dev_map} 📊")  # {'Rakesh': 6, 'Kiran': 5}


# ⚡ 4. GENERATOR EXPRESSION
# Goal: Create a "lazy" iterable that calculates values only when needed.
# Use Case: Processing millions of items without crashing your RAM.

# Syntax: Same as list comprehension but uses () instead of []
large_sum_gen = (x**2 for x in range(1000000))

print(f"Generator Object: {large_sum_gen} 🔋")
# Note: It hasn't calculated the values yet. It's ready when you are!
print(f"First result from generator: {next(large_sum_gen)}")
