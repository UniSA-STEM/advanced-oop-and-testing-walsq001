"""
File: enclosure.py
Description: A brief description of this Python module.
Author: Scott Quinton Walker
ID: 110441860
Username: walsq001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random

class Enclosure:
    def __init__(self, type):
        self.__length = random.randint(50, 100)
        self.__width = random.randint(50, 100)
        self.__total_area = self.__length * self.__width
        self.__cleanliness = 0
        self.__animals = []
        self.__type = type

    def __str__(self):
        if self.__animals:
            animals_str = "\n".join(str(animal) for animal in self.__animals)
        else:
            animals_str = None

        return (f"\nEnclosure type: {self.__type}\n"
                f"Enclosure length: {self.__length}\n"
                f"Enclosure width: {self.__width}\n"
                f"Total area: {self.__total_area}\n"
                f"\n--- Enclosure animals --- \n"
                f"{animals_str}"
                )

    def __iter__(self):
        return iter(self.__animals)

    def add_animal(self, animal):
        self.__animals.append(animal)

    def remove(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)

class Savannah(Enclosure):
    def __init__(self):
        super().__init__("Savannah")
