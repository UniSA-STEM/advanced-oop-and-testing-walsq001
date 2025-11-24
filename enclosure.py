"""
File: enclosure.py
Description: Enclosure classes with species-exclusive rule and cleanliness tracking.
Author: Scott Quinton Walker
ID: 110441860
Username: walsq001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random

class Enclosure:
    enclosure_ID = 0

    def __init__(self, habitat_type):
        self.__enclosure_ID = Enclosure.enclosure_ID
        Enclosure.enclosure_ID += 1
        self.__length = random.randint(300, 500)
        self.__width = random.randint(300, 500)
        self.__total_area = self.__length * self.__width
        self.__cleanliness = 100 # 0 = dirty, 100 = spotless
        self.__animals = []
        self.__type = habitat_type
        self.__allowed_species = None

    def __iter__(self):
        return iter(self.__animals)
    def __len__(self):
        return len(self.__animals)

    # Getters + setters
    def get_type(self):
        return self.__type
    def get_cleanliness(self):
        return self.__cleanliness
    def get_id(self):
        return self.__enclosure_ID

    # Core behaviours
    def add_animal(self, animal):
        # Habitat must match enclosure type
        if animal.get_habitat() != self.get_type():
            print(f"Cannot add {animal.get_species()} to {self.get_type()} enclosure.\n"
                  f"(animal habitat is {animal.get_habitat()}.)")
            return False

        # First animal sets the species for this enclosure
        if not self.__animals:
            self.__allowed_species = animal.get_species()
            self.__animals.append(animal)
            return True

        # Subsequent animals must match the allowed species
        if animal.get_species() == self.__allowed_species:
            self.__animals.append(animal)
            return True

        print(f"Cannot add {animal.get_species()} into this enclosure.\n"
              f"This enclosure is for {self.__allowed_species} only.")
        return False

    def remove(self, animal):
        if animal in self.__animals:
            if animal.under_treatment():
                print(f"Cannot remove {animal.get_name()} from this enclosure (under treatment).\n")
                return False
            self.__animals.remove(animal)
            if not self.__animals:
                self.__allowed_species = None
            return True
        return False

    def dirty(self, amount=5):
        self.__cleanliness = max(0, self.__cleanliness - amount)
        return self.__cleanliness
    def clean(self, effort=20):
        self.__cleanliness = min(100, self.__cleanliness + effort)
        return self.__cleanliness

class Savannah(Enclosure):
    def __init__(self):
        super().__init__("Savannah")

class Aviary(Enclosure):
    def __init__(self):
        super().__init__("Aviary")

class Wetlands(Enclosure):
    def __init__(self):
        super().__init__("Wetlands")