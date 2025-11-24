"""
File: animal.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Animal:
    def __init__(self, name, species, age, diet):
        # Basic details that every animal in the zoo should have
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__health_issues = [] # List to store any health problems

    def get_name(self):
        # Returns the animal’s name
        return self.__name

    def get_species(self):
        # Returns the animal’s species (e.g., Lion, Snake, Bird)
        return self.__species

    def eat(self):
        # Simple behaviour all animals share
        print(self.__name + " is eating " + self.__diet + ".")

    def sleep(self):
        # Another basic behaviour shared by all animals
        print(self.__name + " is sleeping peacefully.")

    def make_sound(self):
        # Default sound — this will be overridden in subclasses
        print(self.__name + " makes a sound.")

    def add_health_issue(self, issue, severity, treatment):
        # Add a new health issue to the list for this animal
        self.__health_issues.append({
            "issue": issue,
            "severity": severity,
            "treatment": treatment
        })

    def show_health_record(self):
        # Display all health issues recorded for the animal
        print("Health records for " + self.__name + ":")
        if not self.__health_issues:
            print("No health issues reported.")
        else:
            for i in self.__health_issues:
                print("- " + i["issue"] + " | Severity: " + i["severity"] +
                      " | Treatment: " + i["treatment"])