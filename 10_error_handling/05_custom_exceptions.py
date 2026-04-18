# 🚨 Custom exception (your own error type)
class OutOfIngredientsError(Exception):
    pass  # 🧱 No extra logic, just a custom name for the error


def make_chai(milk, sugar):
    # 🔍 Check if any ingredient is missing
    if milk == 0 or sugar == 0:
        # 🚨 Raise custom error if ingredients are not available
        raise OutOfIngredientsError("Missing milk or sugar")

    # ☕ If everything is available
    print("Chai is ready...")


# ▶️ Call the function
make_chai(0, 1)  # ❌ milk = 0 → will raise error
