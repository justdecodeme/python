# zip() is a built-in function that returns an iterator of tuples containing the values of the iterables passed to it.
# each item is a tuple of (value1, value2, value3, ...)
# each item must be a number

print("...........")
for value1, value2, value3 in zip(range(5), range(10), range(15)):
    print(value1, value2, value3)  # 0 0 0, 1 1 1, 2 2 2, 3 3 3, 4 4 4
