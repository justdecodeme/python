# enumerate() is a built-in function that returns an iterator of tuples containing the index and the value of an iterable.
# start is an optional parameter that specifies the starting value of the index.
# each item is a tuple of (index, value)

print("...........")
for index, value in enumerate(range(5)):
    print(index, value)  # 0 0, 1 1, 2 2, 3 3, 4 4

print("...........")
for index, value in enumerate(range(5), start=1):
    print(index, value)  # 1 0, 2 1, 3 2, 4 3, 5 4

print("...........")
for index, value in enumerate(range(5), start=10):
    print(index, value)  # 10 0, 11 1, 12 2, 13 3, 14 4
