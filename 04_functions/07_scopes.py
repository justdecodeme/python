counter = 0  # 🌍 Global

print("\n----- Scopes -----\n")


def increment_demo():
    global counter  # `global` Used inside a function to modify a variable in the Global 🌍 scope.
    counter += 1  # ⚡ Without 'global', this would throw an error

    message = "Hello"  # 🏠 Enclosing

    def change_message():
        nonlocal message  # `nonlocal` Used in nested functions to modify a variable in the Enclosing 🏠 scope.
        message = (
            "Hi"  # ⚡ Without 'nonlocal', it would just create a new local variable
        )

    change_message()
    print(message)  # Output: Hi


increment_demo()
print(counter)  # Output: 1
