"""
File: healthRecord.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class HealthRecord:
    def __init__(self, animal_name, issue, date, severity, treatment):
        self.__animal_name = animal_name
        self.__issue = issue
        self.__date = date
        self.__severity = severity
        self.__treatment = treatment

    def show_record(self):
        print("Health Report for " + self.__animal_name)
        print("Issue: " + self.__issue)
        print("Date: " + self.__date)
        print("Severity: " + self.__severity)
        print("Treatment: " + self.__treatment)
