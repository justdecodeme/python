# 🚨 Custom exception for invalid chai flavor
class InvalidChaiError(Exception):
    pass  # 🧱 Just defining a new error type


def bill(flavor, cups):
    # 📋 Menu with prices
    menu = {"masala": 20, "ginger": 40}

    try:
        # 🔍 Check if flavor exists in menu
        if flavor not in menu:
            # 🚨 Raise custom error if flavor is not available
            raise InvalidChaiError("That chai is not available")

        # 🔍 Validate cups is an integer
        if not isinstance(cups, int):
            # 🚨 Raise built-in error if wrong type
            raise TypeError("Number of cups must be an integer")

        # 🧮 Calculate total bill
        total = menu[flavor] * cups

        # 🧾 Print bill
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")

    except Exception as e:
        # ❌ Catch any error (custom or built-in)
        print("Error:", e)

    finally:
        # 🙏 Always runs (success or error)
        print("Thank you for visiting chaicode!")


# ▶️ Test cases

bill("mint", 2)  # ❌ Invalid flavor → custom error
bill("masala", "three")  # ❌ Wrong type → TypeError
bill("ginger", 3)  # ✅ Valid → bill printed
