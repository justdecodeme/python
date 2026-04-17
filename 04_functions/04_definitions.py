# 🏗️ Function Basics and Argument Handling

# 1. Standard Function Declaration
# Use 'def' keyword followed by snake_case name.
def fun():
    """Simple function with no parameters."""
    print("Inside function")


# Calling the function
fun()

print("\n" + "-" * 20 + "\n")


# 2. *args: Arbitrary Arguments (The "Rest Parameter" in JS: ...args)
# *args allows you to pass a variable number of non-keyword arguments.
# Inside the function, 'argv' is treated as a TUPLE.
def my_fun_1(*argv):
    print(f"Type of argv: {type(argv)}")  # Useful to see it's a tuple
    for arg in argv:
        print(arg)


print("Result of *args (Pass as many values as you want):")
my_fun_1("Hello", "Welcome", "to", "Python")

print("\n" + "-" * 20 + "\n")


# 3. **kwargs: Arbitrary Keyword Arguments
# Allows you to pass a variable number of "key=value" pairs.
# Inside the function, 'kwargs' is treated as a DICTIONARY (Object).
def my_fun_2(**kwargs):
    print(f"Type of kwargs: {type(kwargs)}")  # It's a dict!
    for key, value in kwargs.items():
        # Using f-strings (Modern Python 3.6+) is preferred over % formatting
        print(f"{key} == {value}")


print("Result of **kwargs (Pass key-value pairs):")
my_fun_2(first="Frontend", role="Senior Engineer", company="Lenovo")

print("\n" + "-" * 20 + "\n")

# 4. Object Identity and "Pass by Object Reference"
# In Python, everything is an object. id() returns the memory address.


def check_identity(x):
    print(f"Value received: {x} | Memory ID: {id(x)}")


# Driver's code
val = 12
print(f"Value passed: {val} | Memory ID: {id(val)}")
check_identity(val)

# Note: If the IDs match, they point to the exact same object in memory!
