# 🔭 Scoping: Global vs Local variables
# Where does your variable live? 🏡

print("...........")

global_var = "I am everywhere! 🌍"


def shadow():
    local_var = "I am only here! 🏠"
    print(local_var)


shadow()
print(global_var)
# print(local_var) # NameError: name 'local_var' is not defined
