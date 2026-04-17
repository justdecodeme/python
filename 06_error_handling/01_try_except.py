# 🚨 Try/Except: Error catching
# Don't let your program crash! 🚑

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! You can't divide by zero! 💥")
finally:
    print("This runs no matter what! 🏁")
