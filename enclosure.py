"""
File: enclosure.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Enclosure:
    def __init__(self, name, env_type, size):
        self.__name = name
        self.__env_type = env_type
        self.__size = size
        self.__cleanliness = "Clean"
        self.__animals = []

    def get_name(self):
        return self.__name

    def add_animal(self, animal):
        if len(self.__animals) == 0:
            self.__animals.append(animal)
            print(animal.get_name() + " added to " + self.__name + ".")
        else:
            species = self.__animals[0].get_species()
            if animal.get_species() == species:
                self.__animals.append(animal)
                print(animal.get_name() + " added to " + self.__name + ".")
            else:
                print("Cannot mix species in " + self.__name + ".")

    def remove_animal(self, name):
        for a in self.__animals:
            if a.get_name() == name:
                self.__animals.remove(a)
                print(name + " removed from " + self.__name + ".")
                return
        print(name + " not found in " + self.__name + ".")

    def clean_enclosure(self):
        self.__cleanliness = "Clean"
        print(self.__name + " cleaned.")

    def list_animals(self):
        for a in self.__animals:
            print("- " + a.get_name() + " (" + a.get_species() + ")")

    def show_status(self):
        print("Enclosure: " + self.__name + " | Type: " + self.__env_type +
              " | Cleanliness: " + self.__cleanliness)
        if not self.__animals:
            print("  (empty)")
        else:
            print("  Animals: " + ", ".join([a.get_name() for a in self.__animals]))
