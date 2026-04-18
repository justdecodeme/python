# 📝 Lists: Like JS Arrays
# Ordered, mutable collections of items 🎒

print("...........")
inventory = ["sword ⚔️", "shield 🛡️", "potion 🧪"]
inventory.append("map 🗺️")
print(f"Inventory: {inventory}")
print(type(inventory))  # <class 'list'>

# List: containing TUPLES
# Each tuple acts as a fixed "record"
staff = [("Ram", 16), ("Zara", 17), ("Raj", 15)]

print("...........")
print(type(staff))  # <class 'list'>
print(type(staff[0]))  # <class 'tuple'>
