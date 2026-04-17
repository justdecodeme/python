# 📚 Standard Library: Math, Random, OS, Sys
# Everything Python gives you out of the box! 🎁

import math
import random
import my_module

# 🎯 Python's Built-in Functions vs. Standard Library

# 1. Built-in Functions (Always available, no import needed)
# These are the most basic tools that come with the Python interpreter itself.
# Examples: print(), len(), type(), id(), range(), input(), max(), min()

print("\n--- Built-in Functions ---")
print(f"Length of 'Python': {len('Python')}")  # len() is built-in

# 2. Standard Library Modules (Need to be imported)
# These are collections of functions and classes organized into modules.
# They extend Python's capabilities (e.g., math operations, file handling, web requests).
# Examples: math, random, os, sys, datetime, json, requests (external)

print("\n--- Standard Library Modules ---")
# We needed to 'import math' to use math.pi
print(f"Pi is roughly {math.pi} 🥧")
print(f"Random number: {random.randint(1, 10)} 🎲")

# 3. Third-Party Libraries (Need to be installed via pip)
# These are external packages created by the community.
# You must install them first (e.g., pip install requests).
# Example: requests, numpy, pandas, flask, django

# To use 'requests', you would first run: pip install requests
# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)

# 4. Custom Modules
# These are modules created by you.
# Example: my_module.py

print("\n--- Custom Modules ---")
print(my_module.custom_function())
