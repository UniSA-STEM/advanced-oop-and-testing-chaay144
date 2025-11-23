"""
File: staff.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def perform_duty(self, duty, target):
        if self.__role == "Zookeeper" and duty == "feed":
            print(self.__name + " is feeding " + target.get_name() + ".")
        elif self.__role == "Veterinarian" and duty == "check":
            print(self.__name + " is checking the health of " + target.get_name() + ".")
        elif duty == "clean":
            print(self.__name + " is cleaning the enclosure " + target + ".")
        else:
            print(self.__name + " cannot perform this duty.")
