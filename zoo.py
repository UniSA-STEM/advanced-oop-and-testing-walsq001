"""
File: zoo.py
Description: Zoo manager class to coordinate animals,
            enclosures, and staff.
Author: Scott Quinton Walker
ID: 110441860
Username: walsq001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Zoo:
    def __init__(self, name="Simone's Zoo"):
        self.__name = name
        self.__animals = []
        self.__enclosures = []
        self.__staff = []

    # --- Add entities ---
    def add_animal(self, animal):
        self.__animals.append(animal)

    def add_enclosure(self, enclosure):
        self.__enclosures.append(enclosure)

    def add_staff(self, staff):
        self.__staff.append(staff)

    def animals(self):
        return list(self.__animals)
    def enclosures(self):
        return list(self.__enclosures)
    def staff(self):
        return list(self.__staff)

    # Enclosure lifecycle
    def create_enclosure(self, enclosure_class):
        enclosure = enclosure_class()
        self.add_enclosure(enclosure)
        return enclosure

    def remove_enclosure(self, enclosure):
        if enclosure in self.__enclosures:
            # Check if animals are still inside
            if len(enclosure) > 0:
                print(f"Cannot remove {enclosure.get_type()} enclosure; it still contains animals.")
                return False
            self.__enclosures.remove(enclosure)
            print(f"Removed {enclosure.get_type()} enclosure")
            return True
        return False

    # --- Assignments ---
    def assign_animal_to_enclosure(self, animal, enclosure):
        return enclosure.add_animal(animal)

    def assign_staff_to_enclosure(self, staff, enclosure):
        staff.assign_enclosure(enclosure)

    def assign_staff_to_animal(self, animal, staff):
        staff.assign_animal(animal)

    # --- Transfers ---
    def transfer_animal(self, from_enclosure, to_enclosure, animal):
        if animal.under_treatment():
            print(f"Cannot transfer {animal.get_name()} (under treatment)")
            return False
        if from_enclosure.remove(animal):
            if to_enclosure.add_animal(animal):
                print(f"Transferred {animal.get_name()} to {to_enclosure.get_type()} enclosure.")
                return True
            else:
                # rollback if destination rejects
                from_enclosure.add_animal(animal)
        else:
            print(f"Transfer failed; {animal.get_name()} not removable from source.")
        return False

    def place_animal(self, animal, enclosure_class):
        # Try existing enclosures of that type
        for e in self.__enclosures:
            if isinstance(e, enclosure_class):
                if e.add_animal(animal):
                    self.__animals.append(animal)
                    return e
        # If none accepted, create a new enclosure
        new_enclosure = self.create_enclosure(enclosure_class)
        new_enclosure.add_animal(animal)
        self.__animals.append(animal)
        return new_enclosure

    # --- Daily routines ---
    def daily_feed(self):
        # If keepers have assigned enclosures, use them; otherwise feed all
        for s in self.__staff:
            if s.get_role() == "Zookeeper":
                assigned = s.get_assigned_enclosures()
                enclosures = assigned if assigned else self.__enclosures
                for e in enclosures:
                    for a in e:
                        print(f"{s.get_name()} fed {a.get_name()}. Cleanliness now {e.get_cleanliness()}")
                        s.feed(a, amount=2)
                        e.dirty(amount=3)

    def daily_clean(self):
        for s in self.__staff:
            if s.get_role() == "Zookeeper":
                assigned = s.get_assigned_enclosures()
                enclosures = assigned if assigned else self.__enclosures
                for e in enclosures:
                    print(f"{s.get_name()} cleaned {e.get_type()} enclosure. (cleanliness: {e.get_cleanliness()})")
                    s.clean(e, effort=30)

    def run_daily_routines(self):
        print("\n--- Daily feeding ---")
        self.daily_feed()
        print("\n--- Daily cleaning ---")
        self.daily_clean()

    # --- Reports ---
    def report_animals_by_species(self):
        by_species = {}
        for a in self.__animals:
            by_species.setdefault(a.get_species(), []).append(a.get_name())
        return by_species

    def report_enclosure_status(self):
        return [(e, e.get_cleanliness(), len(list(e))) for e in self.__enclosures]

    def report_health_active(self):
        lines = []
        for a in self.__animals:
            actives = [str(r) for r in a.get_health_records() if r.active]
            if actives:
                lines.append((a.get_name(), a.get_species(), actives))
        return lines

    def print_reports(self):
        print(f"\nAnimals by species:")
        for species, names in self.report_animals_by_species().items():
            print(f"{species}: {', '.join(names)}")

        print(f"\nEnclosure status:")
        for enclosure, cleanliness, count in self.report_enclosure_status():
            print(f"{enclosure.get_type()} {enclosure.get_id()}- Cleanliness:{cleanliness}\n"
                  f"Animals: {count}")

        print("\nActive health cases:")
        for line in self.report_health_active():
            print(" " + line.replace("\n", "\n "))