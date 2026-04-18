# 🛑 Sets: Unique collections
# No duplicates allowed! 🚫👯‍♀️

print("...........")
unique_colors = {"red 🔴", "green 🟢", "blue 🔵"}
unique_colors.add("red 🔴")  # Won't be added again!
print(f"Unique colors: {unique_colors}")
print(type(unique_colors))  # <class 'set'>

print("...........")
# This is the constructor method. It is the most versatile way to create a set.
my_siblings = set(["s1", "s2", "s3"])
print(f"My siblings: {my_siblings}")
print(type(my_siblings))  # <class 'set'>

print("...........")
my_list = [1, 2, 2, 3]
unique_set = set(my_list)
print(f"Unique set: {unique_set}")  # Unique set: {1, 2, 3}
print(type(unique_set))  # <class 'set'>

print("...........")
not_a_set = {}
print(type(not_a_set))  # <class 'dict'> ⬅️ Watch out for this!
