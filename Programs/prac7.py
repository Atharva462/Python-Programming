# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

    def __str__(self):
        return f"Animal: {self.name}"

# Derived class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the base class
        self.breed = breed

    def speak(self):
        return "Woof!"

    def __str__(self):
        return f"Dog: {self.name}, Breed: {self.breed}"

# Another derived class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the constructor of the base class
        self.color = color

    def speak(self):
        return "Meow!"

    def __str__(self):
        return f"Cat: {self.name}, Color: {self.color}"

# Demonstration
def main():
    # Create instances of Dog and Cat
    dog = Dog(name="Buddy", breed="Golden Retriever")
    cat = Cat(name="Whiskers", color="Black")

    # Use methods from base and derived classes
    print(dog)  # Output: Dog: Buddy, Breed: Golden Retriever
    print(dog.speak())  # Output: Woof!
    print(cat)  # Output: Cat: Whiskers, Color: Black
    print(cat.speak())  # Output: Meow!

if __name__ == "__main__":
    main()
