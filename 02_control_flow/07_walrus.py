print("\n----- Walrus Operator -----\n")

name = "Rakesh"
if (n := len(name)) > 5:
    print(f"Name is too long ({n} characters)")


print("...........")


def heavy_calculation(x):
    # Imagine this takes a lot of CPU power
    return x**2


numbers = [2, 5, 8, 10]

# Standard: We call heavy_calculation twice (once for filter, once for the value)
results = [heavy_calculation(num) for num in numbers if heavy_calculation(num) > 20]

# Walrus: We call it once, store the result in 'res', and use it twice
results = [res for num in numbers if (res := heavy_calculation(num)) > 30]
# ^ list comprehension + assignment inside condition

print(results)

print("...........")

# The loop will keep running as long as the input isn't 'quit'
while (command := input("Enter command: ")) != "quit":
    print(f"Executing: {command}")
