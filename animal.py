"""
File: animal.py
Description: A brief description of this Python module.
Author: Scott Quinton Walker
ID: 110441860
Username: walsq001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random

MAX_HUNGER = 5
MAX_TIRED = 5

class Animal:
    # Global Variables for each animal
    id_counter = 0
    MASTER_NAMES = []
    available_names = []

    def __init__(self, name, category,
                 species, diet, habitat,
                 sound, hunger=0, tired=0):
        # Create a unique identifier for each animal populating the zoo
        self.__id = Animal.id_counter
        Animal.id_counter += 1
        # Broad attributes
        self.__name = name
        self.__category = category
        self.__species = species # TODO: incorporate species; penguin; rosella; etc.
        # Behavioural attributes
        self.__age = random.randint(1, 20)
        self.__diet = diet # TODO: Ensure eat method utilises appropriate hierarchy
        self.__habitat = habitat # TODO: Import enclosure, ensure descendants populate appropriate habitats
        self.__sound = sound
        self.__hunger = hunger
        self.__tired = tired

    def __str__(self):
        return (f"\nID: {self.__id}, Name: {self.__name}, Age: {self.__age}\n"
                f"Species: {self.__species}, Category: {self.__category}\n"
                f"Habitat: {self.__habitat}, Diet: {self.__diet}\n"
                f"Sound: {self.__sound}")

    @classmethod
    def release(cls, name):
        # cls points to descendant classes
        if name not in cls.available_names and name in cls.MASTER_NAMES:
            cls.available_names.append(name)

    def sleep(self):
        # TODO: Develop this function, incorporate an attribute
        pass

    def make_sound(self):
        # TODO: Develop this function so subclasses utilise their own noise.
        pass

    def eat(self):
        # TODO: Develop this function so subclasses utilise their own diet.
        pass

    def get_name(self):
        return self.__name
    def get_species(self):
        return self.__species
    def get_habitat(self):
        return self.__habitat

"""
TODO: Program subclasses underneath each category of animal.
"""

class Mammal(Animal):
    def __init__(self, name, species, diet, habitat, sound):
        super().__init__(name,"Mammal", species, diet, habitat, sound)

class Lion(Mammal):
    MASTER_NAMES = [
        "Simba", "Nala", "Mufasa",
        "Scar", "Leo"
    ]
    available_names = MASTER_NAMES.copy()
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
    MASTER_NAMES = [
        "Elly", "Stampy", "Dumbo",
        "Bigfoot", "Peanut"
    ]
    available_names = MASTER_NAMES.copy()
    def __init__(self, name=None):
        chosen_name = random.choice(Elephant.available_names)
        Elephant.available_names.remove(chosen_name)
        super().__init__(
            chosen_name,
            "Elephant",
            "Herbivore",
            "Savannah",
            "Brrrrr!"
        )

class Kangaroo(Mammal):
    MASTER_NAMES = [
        "Skippy the Bush Kangaroo", "Hopscotch",
        "Matilda", "Sheila", "Thumper"
    ]
    available_names = MASTER_NAMES.copy()
    def __init__(self, name=None):
        chosen_name = random.choice(Kangaroo.available_names)
        Kangaroo.available_names.remove(chosen_name)
        super().__init__(
            chosen_name,
            "Kangaroo",
            "Herbivore",
            "Savannah",
            "Thump!"
        )

class Reptile(Animal):
    def __init__(self, name, species, diet, habitat, sound):
        super().__init__(name, "Reptile", species, diet, habitat, sound)

class Crocodile(Reptile):
    MASTER_NAMES = ["Ali", "Snappy", "Niblet", "Chomper", "Raptor"]
    available_names = MASTER_NAMES.copy()
    def __init__(self, name=None):
        chosen_name = random.choice(Crocodile.available_names)
        Crocodile.available_names.remove(chosen_name)
        super().__init__(
            chosen_name,
            "Crocodile",
            "Carnivore",
            "Wetlands",
            "Snap!"
        )

class Turtle(Reptile):
    MASTER_NAMES = ["Leonardo", "Donatello", "Raphael", "Michelangelo", "Splinter"]
    available_names = MASTER_NAMES.copy()
    def __init__(self, name=None):
        chosen_name = random.choice(Turtle.available_names)
        Turtle.available_names.remove(chosen_name)
        super().__init__(
            chosen_name,
            "Turtle",
            "Herbivore",
            "Wetlands",
            "Grunt!"
        )

class Bird(Animal):
    def __init__(self, name, species, diet, habitat, sound):
        super().__init__(name, "Bird", species, diet, habitat, sound)

class Rosella(Bird):
    MASTER_NAMES = ["Rosie", "Ronnie", "Tweedledee", "Tweedledum"]
    available_names = MASTER_NAMES.copy()
    def __init__(self, name=None):
        chosen_name = random.choice(Rosella.available_names)
        Rosella.available_names.remove(chosen_name)
        super().__init__(
            chosen_name,
            "Rosella",
            "Herbivore",
            "Aviary",
            "Sqwuak!"
        )

