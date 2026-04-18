def brew_chai(flavor):
    # 🔍 Check if the flavor is NOT in allowed list
    if flavor not in ["masala", "ginger", "elaichai"]:
        # 🚨 Raise an error if flavor is invalid
        raise ValueError("Unsupported chai flavor...")

    # ☕ If valid, prepare the chai
    print(f"Brewing {flavor} chai...")


# ▶️ Try calling the function with an invalid flavor
brew_chai("mint")  # ❌ Not in list → will raise error
