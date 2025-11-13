"""
File: animal.py
Description: A brief description of this Python module.
Author: Scott Quinton Walker
ID: 110441860
Username: walsq001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random

class Animal:
    id_counter = 0
    def __init__(self, name, category, species, diet, habitat):
        self.__id = Animal.id_counter
        Animal.id_counter += 1

        self.__name = name
        self.__category = category # TODO: broaden categories; mammal; reptile; etc.
        self.__species = species # TODO: incorporate species; penguin; rosella; etc.
        self.__age = random.randint(1, 20)
        self.__diet = diet
        self.__habitat = habitat

    def __str__(self):
        return (f"ID: {self.__id}, Name: {self.__name}, Age: {self.__age}\n"
                f"Species: {self.__species}, Category: {self.__category}\n"
                f"Habitat: {self.__habitat}, Diet: {self.__diet}")

    def sleep(self):
        # TODO: Develop this function, incorporate an attribute
        pass

    def make_sound(self):
        # TODO: Develop this function so subclasses utilise their own noise.
        pass

    def eat(self):
        # TODO: Develop this function so subclasses utilise their own diet.
        pass

    def set_name(self, name):
        self.__name = name

    def set_species(self, species):
        pass

"""
TODO: Program subclasses underneath each category of animal.
"""

class Mammal(Animal):
    def __init__(self, name, species, diet, habitat):
        super().__init__(name,"Mammal", species, diet, habitat)

class Lion(Mammal):
    def __init__(self, name=None):
        names = ["Simba", "Nala", "Mufasa", "Scar", "Leo"]
        chosen_name = random.choice(names)
        super().__init__(
            chosen_name,
            "Lion",
            "Carnivore",
            "Savannah"
        )

class Reptile(Animal):
    def __init__(self):
        super().__init__(None, None, "Reptile")

class Bird(Animal):
    def __init__(self):
        super().__init__(None, None, "Bird")

class Amphibian(Animal):
    def __init__(self):
        super().__init__(None, None, "Amphibian")

class Fish(Animal):
    def __init__(self):
        super().__init__(None, None, "Fish")

class Insect(Animal):
    def __init__(self):
        super().__init__(None, None, "Insect")
