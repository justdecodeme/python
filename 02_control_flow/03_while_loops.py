# 🔄 While Loops: Logical loops
# Keep going until something stops you! 🛑

print("...........")
count = 3
while count > 0:
    print(f"Countdown: {count} ⏳")
    count -= 1
print("Blastoff! 🚀")

# 🧾 Real-world example: Simulating a login system with a while loop
# The loop keeps asking for the password until it matches the correct one

correct_password = "password123"
attempts = 0
max_attempts = 3

print("...........")
while True:  # This creates an infinite loop that we'll break out of manually
    entered_password = input("Enter your password: ")
    attempts += 1

    if attempts == max_attempts:
        print("Too many attempts. Please try again later. ❌")
        break

    if entered_password == correct_password:
        print(f"Access granted! ✅ You logged in after {attempts} attempts.")
        break  # Exit the loop when the password is correct
    else:
        print(
            "Incorrect password.",
            max_attempts - attempts,
            "attempts left",
        )
