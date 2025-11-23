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
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__health_issues = []

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def eat(self):
        print(self.__name + " is eating " + self.__diet + ".")

    def sleep(self):
        print(self.__name + " is sleeping peacefully.")

    def make_sound(self):
        print(self.__name + " makes a sound.")

    def add_health_issue(self, issue, severity, treatment):
        self.__health_issues.append({
            "issue": issue,
            "severity": severity,
            "treatment": treatment
        })

    def show_health_record(self):
        print("Health records for " + self.__name + ":")
        if not self.__health_issues:
            print("No health issues reported.")
        else:
            for i in self.__health_issues:
                print("- " + i["issue"] + " | Severity: " + i["severity"] +
                      " | Treatment: " + i["treatment"])