"""
File: main.py
Description: This module demonstrates most requirements of the assignment.
Author: Scott Quinton Walker
ID: 110441860
Username: walsq001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from animal import Lion, Elephant, Crocodile, Turtle, Rosella
from enclosure import Savannah, Aviary, Wetlands
from staff import Zookeeper, Vet
from zoo import Zoo

def main():
    zoo = Zoo()

    # Staff
    keepers = [Zookeeper() for _ in range(3)]
    vets = [Vet() for _ in range(2)]
    for k in keepers:
        zoo.add_staff(k)
    for v in vets:
        zoo.add_staff(v)

    # Animals
    lions = [Lion() for _ in range(4)]
    elephants = [Elephant() for _ in range(2)]
    crocodiles = [Crocodile() for _ in range(4)]
    turtles = [Turtle() for _ in range(2)]
    birds = [Rosella() for _ in range(3)]

    for lion in lions:
        zoo.place_animal(lion, Savannah)
    for elephant in elephants:
        zoo.place_animal(elephant, Savannah)
    for croc in crocodiles:
        zoo.place_animal(croc, Wetlands)
    for t in turtles:
        zoo.place_animal(t, Wetlands)
    for b in birds:
        zoo.place_animal(b, Aviary)

    # Polymorphism demonstration
    print("\nAnimal behaviours:")
    for a in zoo.animals():
        a.make_sound()
        a.eat()
        a.sleep()

    # Daily routines
    zoo.run_daily_routines()

    # Health workflow
    sick_lion = lions[0]
    print(f"\n{vets[0].get_name()} checking {sick_lion.get_name()}...")
    vets[0].health_check(
        sick_lion, "Limping after play",
        severity=2, notes="Rest 3 days"
    )

    print("\nActive health cases:")
    for case in zoo.report_health_active():
        print(f"{case[0]} ({case[1]}):")
        for record in case[2]:
            print(record)

    print("\nAttempting transfer of sick lion:")
    new_savannah = zoo.create_enclosure(Savannah)
    zoo.transfer_animal(zoo.enclosures()[0], new_savannah, sick_lion)

    print("\nClosing health case:")
    vets[0].close_case(sick_lion, notes="Recovered")

    print("\nTransferring recovered lion to a new enclosure:")
    zoo.transfer_animal(zoo.enclosures()[0], new_savannah, sick_lion)

    # Reports
    zoo.print_reports()

if __name__ == "__main__":
    main()

