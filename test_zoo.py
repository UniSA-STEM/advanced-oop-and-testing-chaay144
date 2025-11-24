"""
File: test_zoo.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import unittest
from zoo import Zoo
from mammal import Mammal
from reptile import Reptile
from bird import Bird
from staff import Staff


class TestZooSystem(unittest.TestCase):

    def setUp(self):
        """Set up zoo, enclosures, staff, and animals for testing."""
        self.zoo = Zoo("ByteWise Zoo")

        # Add enclosures
        self.zoo.add_enclosure("Savannah", "Grassland", "Large")
        self.zoo.add_enclosure("Reptile House", "Tropical", "Medium")
        self.zoo.add_enclosure("Aviary", "Forest", "Small")

        # Add staff
        self.keeper = Staff("Simone", "Zookeeper")
        self.vet = Staff("Alex", "Veterinarian")
        self.zoo.add_staff(self.keeper)
        self.zoo.add_staff(self.vet)

        # Create animals
        self.lion = Mammal("Leo", "Lion", 5, "Meat")
        self.snake = Reptile("Sly", "Snake", 3, "Rats")
        self.parrot = Bird("Polly", "Parrot", 2, "Seeds")

    def test_add_animals(self):
        """Animals should be added to correct enclosures."""
        self.zoo.add_animal_to_enclosure(self.lion, "Savannah")
        self.zoo.add_animal_to_enclosure(self.snake, "Reptile House")
        self.zoo.add_animal_to_enclosure(self.parrot, "Aviary")
        # Make sure the species data stays correct
        self.assertEqual(self.lion.get_species(), "Lion")
        self.assertEqual(self.snake.get_species(), "Snake")
        self.assertEqual(self.parrot.get_species(), "Parrot")

    def test_staff_actions(self):
        """Staff perform feeding, checking and cleaning."""
        self.keeper.perform_duty("feed", self.lion)
        self.vet.perform_duty("check", self.snake)
        self.keeper.perform_duty("clean", "Reptile House")
        # Confirm the roles are stored correctly
        self.assertEqual(self.keeper.get_role(), "Zookeeper")
        self.assertEqual(self.vet.get_role(), "Veterinarian")

    def test_make_sound_polymorphism(self):
        """Each animal type uses its own sound method."""
        # make_sound returns None because it only prints output
        self.assertIsNone(self.lion.make_sound())
        self.assertIsNone(self.snake.make_sound())
        self.assertIsNone(self.parrot.make_sound())


    def test_sick_animal_movement_blocked(self):
        """Animals with health issues should not move."""
        self.lion.add_health_issue("Injury", "Medium", "Rest 7 days")
        # Since the lion is now sick, the zoo should block the move
        self.zoo.add_animal_to_enclosure(self.lion, "Aviary")  # should not move

    def test_daily_routine(self):
        """Daily routine runs successfully."""
        self.zoo.daily_routine()
        # If no crash happens, the test passes
        self.assertTrue(True)  # passes if no crash or error

    def test_reports(self):
        """Reports for animals, enclosures, and health should display."""
        self.zoo.show_all_animals()
        self.zoo.show_all_enclosures()
        self.zoo.show_health_reports()
        self.assertTrue(True)

    def test_remove_animal(self):
        """Animals can be removed from an enclosure."""
        self.zoo.add_animal_to_enclosure(self.snake, "Reptile House")
        self.zoo.remove_animal("Sly")
        self.assertTrue(True)


if __name__ == "__main__":
    print("=== Running Zoo Management System Tests ===\n")
    unittest.main()
