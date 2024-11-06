class Person:
    def __init__(self, name, age, gender):
        """Initialize the person's attributes."""
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        """Introduce the person with their name, age, and gender."""
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Creating an instance of the Person class
person_instance = Person("Alice", 30, "Female")

# Calling the introduce method to display the person's information
person_instance.introduce()
