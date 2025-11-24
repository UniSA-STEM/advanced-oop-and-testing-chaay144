"""
File: reptile.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from animal import Animal

class Reptile(Animal):
    # Reptile uses its own version of the sound method (polymorphism)
    def make_sound(self):
        print(self.get_name() + " hisses softly.")

    # Special behaviour only reptiles have
    def shed_skin(self):
        print(self.get_name() + " is sheds its skin.")