# zip() is a built-in function that returns an iterator of tuples containing the values of the iterables passed to it.
# each item is a tuple of (value1, value2, value3, ...)
# each item must be a number

print("...........")
for value1, value2, value3 in zip(range(5), range(10), range(15)):
    print(value1, value2, value3)  # 0 0 0, 1 1 1, 2 2 2, 3 3 3, 4 4 4

# 🧾 Real-world example: Pairing names with their bill amounts using zip()
# zip() combines two lists element-by-element into tuples → (name, bill)
names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

print("...........")
for name, amount in zip(names, bills):
    # 💡 f-string to display each person's payment in a readable format
    print(f"{name} paid {amount} rupees")  # e.g. Hitesh paid 50 rupees
