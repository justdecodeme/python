# 🏗️ Classes: Object-Oriented Programming
# Blueprints for creating objects 🏠

print("\n--- Classes ---")


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof! 🐶")


my_dog = Dog("Buddy")
my_dog.bark()
