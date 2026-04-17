# 🧬 Inheritance: Sharing code between classes
# Passing down traits! 👨‍👦

class Animal:
    def eat(self):
        print("Munch munch munch! 🍲")

class Cat(Animal):
    def meow(self):
        print("Meow! 🐱")

my_cat = Cat()
my_cat.eat() # Inherited from Animal
my_cat.meow()
