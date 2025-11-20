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
    enclosure_ID = 0
    def __init__(self, type):
        self.__enclosure_ID = Enclosure.enclosure_ID
        Enclosure.enclosure_ID += 1
        self.__length = random.randint(50, 100)
        self.__width = random.randint(50, 100)
        self.__total_area = self.__length * self.__width
        self.__cleanliness = 0
        self.__animals = []
        self.__type = type
        self.__allowed_animals = None

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

    def get_type(self):
        return self.__type

    def add_animal(self, animal):
        # If animal habitat is suitable to enclosure type, continue
        if animal.get_habitat() == self.get_type():
            # If no animals in enclosure, add it
            if not self.__animals:
               self.__allowed_animals = animal.get_species()
               self.__animals.append(animal)
            # Else type check there isn't a different species
            # Add it to the enclosure if the same species
            # Return print statement otherwise
            else:
                if animal.get_species() == self.__allowed_animals:
                    self.__animals.append(animal)
                else:
                    print(f"Cannot add {animal.get_species()} into this enclosure.\n"
                          f"Only {self.__allowed_animals}'s are allowed")
        else:
            print(f"Cannot add {animal.get_species()} into this enclosure.\n")

    def remove(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)

class Savannah(Enclosure):
    def __init__(self):
        super().__init__("Savannah")

class Aviary(Enclosure):
    def __init__(self):
        super().__init__("Aviary")