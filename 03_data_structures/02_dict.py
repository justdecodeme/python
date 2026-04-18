# 📖 Dictionaries: Like JS Objects
# Key-value pairs for structured data 🗂️

print("...........")
player = {"name": "Hero", "level": 10, "class": "Knight 🤺"}
print(player)  # {'name': 'Hero', 'level': 10, 'class': 'Knight 🤺'}
print(type(player))  # <class 'dict'>

print("...........")
# Accessing values
print(player["name"])  # Hero
print(player.get("level"))  # 10

print("...........")
# Adding/Updating values
player["gold"] = 100
player["level"] = 11
print(player)  # {'name': 'Hero', 'level': 11, 'class': 'Knight 🤺', 'gold': 100}

print("...........")
# Removing values
del player["gold"]
print(player)  # {'name': 'Hero', 'level': 11, 'class': 'Knight 🤺'}

print("...........")
# Iterating through a dictionary
for key, value in player.items():
    print(f"{key}: {value}")

print("...........")
print("keys: ", player.keys())  # dict_keys(['name', 'level', 'class'])
print("values: ", player.values())  # dict_values(['Hero', 11, 'Knight 🤺'])
print(
    "items: ", player.items()
)  # dict_items([('name', 'Hero'), ('level', 11), ('class', 'Knight 🤺')])
