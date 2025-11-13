"""
File: main.py
Description: A brief description of this Python module.
Author: Scott Quinton Walker
ID: 110441860
Username: walsq001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from animal import Lion

lions = []
count = 0

while count < 6 and Lion.available_names:
    lion = Lion()
    lions.append(lion)
    print(lion)
    count += 1

print("\nSummary: ")
for lion in lions:
    print(f"- {lion._Animal__name}")