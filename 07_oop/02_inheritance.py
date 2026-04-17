# 🧬 Inheritance: Sharing code between classes
# Passing down traits! 👨‍👦

print("\n--- Inheritance ---")


class Animal:
    def eat(self):
        print("Munch munch munch! 🍲")


class Cat(Animal):
    def meow(self):
        print("Meow! 🐱")


class Dog(Animal):
    def bark(self):
        print("Woof! 🐶")

    def eat(self):
        print("Bone! 🦴")


print("\nCat:")
my_cat = Cat()
my_cat.eat()  # Inherited from Animal
my_cat.meow()

print("\nDog:")
my_dog = Dog()
my_dog.eat()  # Overridden from Animal
my_dog.bark()
