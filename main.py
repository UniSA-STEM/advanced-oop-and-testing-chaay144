"""
File: main.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from zoo import Zoo
from mammal import Mammal
from reptile import Reptile
from bird import Bird
from staff import Staff
from healthRecord import HealthRecord


zoo = Zoo("ByteWise Zoo")

# Create animals
lion = Mammal("Leo", "Lion", 5, "Meat")
snake = Reptile("Sly", "Snake", 3, "Rats")
parrot = Bird("Polly", "Parrot", 2, "Seeds")

# Create enclosures
savannah = zoo.add_enclosure("Savannah Habitat", "Savannah", "Large")
reptile_house = zoo.add_enclosure("Reptile House", "Tropical", "Medium")
aviary = zoo.add_enclosure("Aviary", "Forest", "Small")

# Create staff
keeper = Staff("Simone", "Zookeeper")
vet = Staff("Alex", "Veterinarian")
zoo.add_staff(keeper)
zoo.add_staff(vet)

# Assign animals
zoo.add_animal_to_enclosure(lion, "Savannah Habitat")
zoo.add_animal_to_enclosure(snake, "Reptile House")
zoo.add_animal_to_enclosure(parrot, "Aviary")

# Staff performing duties
keeper.perform_duty("feed", lion)
keeper.perform_duty("clean", "Reptile House")
vet.perform_duty("check", parrot)

# Add health issue (prevents movement)
lion.add_health_issue("Leg injury", "Medium", "Rest and treatment")
record = HealthRecord(lion.get_name(), "Leg injury", "2025-11-10", "Medium", "Rest for 7 days")
zoo.add_health_record(record)

# Try to move sick animal (should fail)
zoo.add_animal_to_enclosure(lion, "Aviary")

# Generate reports
zoo.show_all_animals()
zoo.show_all_enclosures()
zoo.show_health_reports()

# Daily routine
zoo.daily_routine()


