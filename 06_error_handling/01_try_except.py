# 🚨 Try/Except: Error catching
# Don't let your program crash! 🚑

print("\n--- Try/Except ---")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! You can't divide by zero! 💥")
finally:
    print("This runs no matter what! 🏁")

print("\n--- Try/Except/Else ---")
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a number. ❌")
else:
    print(f"You entered: {num} ✅")


print("\n--- Try/Except/Else/Finally ---")
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a number. ❌")
else:
    print(f"You entered: {num} ✅")
finally:
    print("Done! 🏁")
