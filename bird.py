"""
File: bird.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from animal import Animal

class Bird(Animal):
    def make_sound(self):
        print(self.get_name() + " chirpping")

    def fly(self):
        print(self.get_name() + " is flying high.")
