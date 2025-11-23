"""
File: zoo.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from enclosure import Enclosure

class Zoo:
    def __init__(self, name):
        self.__name = name
        self.__enclosures = []
        self.__staff = []
        self.__health_records = []

    def add_enclosure(self, name, env_type, size):
        new_enclosure = Enclosure(name, env_type, size)
        self.__enclosures.append(new_enclosure)
        print("Enclosure " + name + " added to " + self.__name + ".")
        return new_enclosure

    def add_staff(self, staff):
        self.__staff.append(staff)
        print(staff.get_name() + " hired as " + staff.get_role() + ".")

    def add_animal_to_enclosure(self, animal, enclosure_name):
        if self.__is_animal_sick(animal):
            print(animal.get_name() + " cannot be moved due to health issues.")
            return
        for enclosure in self.__enclosures:
            if enclosure.get_name() == enclosure_name:
                enclosure.add_animal(animal)
                return
        print("Enclosure " + enclosure_name + " not found.")

    def remove_animal(self, animal_name):
        for enclosure in self.__enclosures:
            enclosure.remove_animal(animal_name)

    def add_health_record(self, record):
        self.__health_records.append(record)

    def show_all_animals(self):
        print("\nAll Animals in the Zoo:")
        for enclosure in self.__enclosures:
            enclosure.list_animals()

    def show_all_enclosures(self):
        print("\nAll Enclosures:")
        for enclosure in self.__enclosures:
            enclosure.show_status()

    def show_health_reports(self):
        print("\nZoo Health Records:")
        if not self.__health_records:
            print("No records available.")
        else:
            for record in self.__health_records:
                record.show_record()

    def daily_routine(self):
        print("\n--- Daily Routine ---")
        for s in self.__staff:
            if s.get_role() == "Zookeeper":
                for e in self.__enclosures:
                    e.clean_enclosure()
            if s.get_role() == "Veterinarian":
                print(s.get_name() + " performs daily health checks.")
        print("Routine complete.\n")

    def __is_animal_sick(self, animal):
        # If animal has any health issues, mark as sick
        return len(animal._Animal__health_issues) > 0