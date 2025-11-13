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
    def __init__(self, name, category, species, diet, habitat, sound):
        self.__id = Animal.id_counter
        Animal.id_counter += 1

        self.__name = name
        self.__category = category # TODO: broaden categories; mammal; reptile; etc.
        self.__species = species # TODO: incorporate species; penguin; rosella; etc.
        self.__age = random.randint(1, 20)
        self.__diet = diet
        self.__habitat = habitat
        self.__sound = sound

    def __str__(self):
        return (f"ID: {self.__id}, Name: {self.__name}, Age: {self.__age}\n"
                f"Species: {self.__species}, Category: {self.__category}\n"
                f"Habitat: {self.__habitat}, Diet: {self.__diet}\n"
                f"Sound: {self.__sound}")

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
    def __init__(self, name, species, diet, habitat, sound):
        super().__init__(name,"Mammal", species, diet, habitat, sound)

class Lion(Mammal):
    available_names = ["Simba", "Nala", "Mufasa", "Scar", "Leo"]
    def __init__(self, name=None):
        chosen_name = random.choice(Lion.available_names)
        Lion.available_names.remove(chosen_name)
        super().__init__(
            chosen_name,
            "Lion",
            "Carnivore",
            "Savannah",
            "Roar!"
        )

class Elephant(Mammal):
    def __init__(self, name=None):
        names = ["Elly", "Stampy", "Dumbo", "Bigfoot", "Peanut"]
        chosen_name = random.choice(names)
        super().__init__(
            chosen_name,
            "Elephant",
            "Herbivore",
            "Savannah",
            "Trumpet"
        )

class Kangaroo(Mammal):
    def __init__(self, name=None):
        names = ["Skippy the Bush Kangaroo", "Hopscotch", "Matilda", "Sheila"]
        chosen_name = random.choice(names)
        super().__init__(
            chosen_name,
            "Kangaroo",
            "Herbivore",
            "Savannah"
        )

class Reptile(Animal):
    def __init__(self, name, species, diet, habitat):
        super().__init__(name, "Reptile", species, diet, habitat)

class Crocodile(Reptile):
    def __init__(self, name=None):
        names = ["Ali", "Snappy", "Niblet", "Chomper", "Raptor"]
        chosen_name = random.choice(names)
        super().__init__(
            chosen_name,
            "Crocodile",
            "Carnivore",
            "Wetlands",
        )

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
