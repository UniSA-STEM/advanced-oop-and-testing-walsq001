"""
File: main.py
Description: A brief description of this Python module.
Author: Scott Quinton Walker
ID: 110441860
Username: walsq001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from animal import Lion, Elephant
from enclosure import Savannah, Aviary

count = 0
enclosure = Savannah()
enclosure2 = Aviary()

while count < 6 and Lion.available_names:
    lion = Lion()
    enclosure.add_animal(lion)
    print(enclosure)
    count += 1

elephant = Elephant()
enclosure2.add_animal(elephant)

print("\nSummary before transfer: ")
for lion in enclosure:
    print(f"- {lion.get_name()}")

# Transfer a lion out of the zoo
for lion in list(enclosure):
    if lion.get_name() == "Mufasa":
        enclosure.remove(lion)
        Lion.release("Mufasa")
        break

print("\nSummary after transfer: ")
for lion in enclosure:
    print(f"- {lion.get_name()}")

print("Available names:", Lion.available_names)