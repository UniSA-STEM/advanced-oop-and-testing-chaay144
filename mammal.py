"""
File: mammal.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from animal import Animal

class Mammal(Animal):
    # Mammals have their own version of the sound they make (polymorphism)
    def make_sound(self):
        print(self.get_name() + " says roar.")

    # Extra behaviour that only mammals have
    def feed_milk(self):
        print(self.get_name() + " is feeding milk to its young.")