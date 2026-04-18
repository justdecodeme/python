# 🌍 GLOBAL SCOPE
# Defined at the top level of the script. Accessible everywhere.
user_name = "Rakesh"

print("\n----- Scopes -----\n")


def outer_function():
    # 🏠 ENCLOSING SCOPE
    # Inside the parent function, but outside the inner function.
    # Similar to a "Closure" in JavaScript.
    role = "Senior Engineer"

    def inner_function():
        # 📍 LOCAL SCOPE
        # Local to just this specific function.
        status = "Learning Python"

        # --- The Search Order ---
        print(f"I am {user_name} (Found in GLOBAL 🌍)")
        print(f"My role is {role} (Found in ENCLOSING 🏠)")
        print(f"Currently: {status} (Found in LOCAL 📍)")

        # 🧱 BUILT-IN SCOPE
        # Names that come pre-loaded with Python (like len, print, sum).
        # We don't define these; Python provides them.
        name_length = len(user_name)
        print(f"Name length is: {name_length} (len() is BUILT-IN 🧱)")

    inner_function()


outer_function()

# ⚠️ SCOPE TRAP:
# Attempting to print(status) here would throw a NameError
# because it only exists in the LOCAL 📍 scope of inner_function.
