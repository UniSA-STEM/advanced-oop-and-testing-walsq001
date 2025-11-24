"""
File: staff.py
Description: Staff module hosts Vet and Zookeeper subclasses
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

    # Assignment
    def assign_enclosure(self, enclosure):
        self.__assigned_enclosures.append(enclosure)

    def assign_animal(self, animal):
        self.__assigned_animals.append(animal)

    # Getters
    def get_name(self):
        return self.__name
    def get_role(self):
        return self.__role
    def get_assigned_enclosures(self):
        return list(self.__assigned_enclosures)
    def get_assigned_animals(self):
        return list(self.__assigned_animals)

    # Basic actions shared by staff
    def feed(self, animal, amount=2):
        return animal.eat(amount)

    def clean(self, enclosure, effort=30):
        enclosure.clean(effort=effort)
        return True

class Vet(Staff):
    def __init__(self):
        name = random.choice(Staff.available_names)
        Staff.available_names.remove(name)
        super().__init__(
            name,
            "Veterinarian"
        )

    def health_check(self, animal, description, severity=1, notes=""):
        from animal import HealthRecord
        if not isinstance(severity, int) or not (1 <= severity <= 5):
            raise ValueError("Severity must be a integer value between 1 and 5.")
        record = HealthRecord(description=description, severity=severity, treatment_notes=notes)
        animal.add_health_record(record)
        print(f"Recorded health issue for {animal.get_name()}:\n"
              f"Description: {description} (severity {severity}\n")
        return record

    def close_case(self, animal, notes=""):
        # close latest active record
        for record in reversed(animal.get_health_records()):
            if record.active:
                record.close(notes)
                print(f"Closed case for {animal.get_name()}.")
                return record
        print(f"No active health record for {animal.get_name()}.")
        return None

    def feed(self, animal, amount=2):
        print(f"Vets cannot feed animals. Assign a zookeeper instead.")
        return False

    def clean(self, enclosure, effort=30):
        print(f"Vets cannot clean enclosures. Assign a zookeeper instead.")
        return False


class Zookeeper(Staff):
    def __init__(self):
        name = random.choice(Staff.available_names)
        Staff.available_names.remove(name)
        super().__init__(
            name,
            "Zookeeper"
        )

