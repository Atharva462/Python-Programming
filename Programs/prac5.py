class Person:
    def __init__(self, name, age):
        # Constructor method to initialize attributes
        self.name = name
        self.age = age

    def display_info(self):
        # Method to display the person's information
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Creating an instance of the Person class
person1 = Person("Atharva", 19)

# Calling the display_info method to show the initialized attributes
person1.display_info()
