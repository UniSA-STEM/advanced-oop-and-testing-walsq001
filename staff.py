"""
File: staff.py
Description: A brief description of this Python module.
Author: Scott Quinton Walker
ID: 110441860
Username: walsq001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
class Staff:
    MASTER_NAMES = ["Sue", "Bill", "Roger", "Homer", "Marge",
                    "Lisa", "Bart", "Fred", "John", "Lou",
                    "George", "Sarah", "Sunny", "Judy"]
    available_names = MASTER_NAMES.copy()
    identifier = 0
    def __init__(self, name, role):
        self.__staff_ID = Staff.identifier
        Staff.identifier += 1
        self.__name = name
        self.__role = role
        self.__assigned_enclosures = []
        self.__assigned_animals = []

    def assign_enclosure(self, enclosure):
        self.__assigned_enclosures.append(enclosure)

    def assign_animal(self, animal):
        self.__assigned_animals.append(animal)

    def get_name(self):
        return self.__name
    def get_role(self):
        return self.__role

class Vet(Staff):
    def __init__(self, name, role):
        name = random.choice(Staff.available_names)
        Staff.available_names.remove(name)
        super().__init__(
            name,
            "Veterinarian"
        )

class Zookeeper(Staff):
    def __init__(self, name, role):
        name = random.choice(Staff.available_names)
        Staff.available_names.remove(name)
        super().__init__(
            name,
            "Zookeeper"
        )

