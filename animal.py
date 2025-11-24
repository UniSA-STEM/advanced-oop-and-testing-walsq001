"""
File: animal.py
Description: The animal module contains relevant attributes and methods
            which underpin the functions of the zoo.
Author: Scott Quinton Walker
ID: 110441860
Username: walsq001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from datetime import datetime

class HealthRecord:
    def __init__(self, description, severity=1, treatment_notes=None):
        self.__date = datetime.now().date()
        self.__description = description
        self.__severity = severity
        self.__treatment_notes = treatment_notes
        self.__active = True

    def close(self, notes=None):
        if notes:
            if self.__treatment_notes:
                self.__treatment_notes += f"; {notes}"
            else:
                self.__treatment_notes = notes
        self.__active = False

    # Getters/properties
    @property
    def date(self):
        return self.__date
    @property
    def description(self):
        return self.__description
    @property
    def severity(self):
        return self.__severity
    @property
    def treatment_notes(self):
        return self.__treatment_notes
    @property
    def active(self):
        return self.__active

    def __str__(self):
        status = "Active" if self.__active else "Closed"
        return (f"{self.__date} | severity: {self.__severity} | Status: {status}"
                f"\nNotes: {self.__treatment_notes or ''} | {self.__description}")

class Animal:
    id_counter = 0

    def __init__(self, name, category,
                 species, diet, habitat,
                 sound):
        # Create a unique identifier for each animal populating the zoo
        self.__id = Animal.id_counter
        Animal.id_counter += 1
        # Broad attributes
        self.__name = name
        self.__category = category
        self.__species = species
        # Behavioural attributes
        self.__age = random.randint(1, 20)
        self.__diet = diet
        self.__habitat = habitat
        self.__sound = sound
        self.__hunger = random.randint(3, 7)
        self.__tired = random.randint(3, 7)
        self.__health_records = []

    def __str__(self):
        under = " (Under treatment)" if self.under_treatment() else ""
        return (f"\nID: {self.__id}, Name: {self.__name}, Age: {self.__age}{under}\n"
                f"Species: {self.__species}, Category: {self.__category}\n"
                f"Habitat: {self.__habitat}, Diet: {self.__diet}")

    # Behaviours
    def sleep(self, hours=8):
        before = self.__tired
        self.__tired = max(0, self.__tired - hours//2)
        print(f"{self.__name} the {self.__species} sleeps {hours}h. Tiredness {before} → {self.__tired}")
        return self.__tired

    def make_sound(self):
        print(f"{self.__name} the {self.__species} makes a sound: {self.__sound}")
        return self.__sound

    def eat(self, amount=2):
        before = self.__hunger
        self.__hunger = max(0, self.__hunger - amount)
        print(f"{self.__name} the {self.__species} eats ({self.__diet}). Hunger {before} → {self.__hunger}")
        return self.__hunger

    # Health
    def add_health_record(self, record):
        if not isinstance(record, HealthRecord):
            raise TypeError("Record must be HealthRecord.")
        self.__health_records.append(record)

    def get_health_records(self):
        return list(self.__health_records)

    def under_treatment(self):
        return any(r.active for r in self.__health_records)

    # Getters
    def get_name(self):
        return self.__name
    def get_species(self):
        return self.__species
    def get_habitat(self):
        return self.__habitat

# Subclasses
class Mammal(Animal):
    def __init__(self, name, species, diet, habitat, sound):
        super().__init__(name,"Mammal", species, diet, habitat, sound)

class Lion(Mammal):
    MASTER_NAMES = [
        "Simba", "Nala", "Mufasa",
        "Scar", "Leo"
    ]
    available_names = MASTER_NAMES.copy()
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
        chosen_name = random.choice(Rosella.available_names)
        Rosella.available_names.remove(chosen_name)
        super().__init__(
            chosen_name,
            "Rosella",
            "Herbivore",
            "Aviary",
            "Sqwuak!"
        )

