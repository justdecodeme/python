# 🧮 Simple Calculator: Tying it all together!
# Let's build something! 🛠️

print("\n--- Interactive Calculator ---")

try:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(f"Result: {num1 + num2} ➕")
    elif op == "-":
        print(f"Result: {num1 - num2} ➖")
    elif op == "*":
        print(f"Result: {num1 * num2} ✖️")
    elif op == "/":
        if num2 == 0:
            print("Can't divide by zero! 🚫")
        else:
            print(f"Result: {num1 / num2} ➗")
    else:
        print("Invalid operator! ❌")

except ValueError:
    print("Invalid input! Please enter numbers. 🤓")
