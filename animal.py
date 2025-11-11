"""
File: animal.py
Description: A brief description of this Python module.
Author: Scott Quinton Walker
ID: 110441860
Username: walsq001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__species = None # TODO: incorporate species; penguin; rosella; etc.
        self.__age = age
        self.__category = None # TODO: broaden categories; mammal; reptile; etc.

    def __str__(self):
        return (f"Name: {self.__name}, Age: {self.__age}, "
                f"Species: {self.__species}, Category: {self.__category}")

    def sleep(self):
        # TODO: Develop this function, incorporate an attribute
        pass

    def make_sound(self):
        # TODO: Develop this function so subclasses utilise their own noise.
        pass

    def eat(self):
        # TODO: Develop this function so subclasses utilise their own diet.
        pass