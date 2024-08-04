import time
import random

class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 50
        self.happiness = 50
        self.health = 50

    def feed(self):
        self.hunger += 10
        print(f"{self.name} has been fed!")

    def play(self):
        if self.hunger > 10:
            self.happiness += 10
            self.hunger -= 10
            print(f"You played with {self.name}!")
        else:
            print(f"{self.name} is too hungry to play!")

    def heal(self):
        if self.health < 100:
            self.health += 10
            print(f"{self.name} is feeling better!")
        else:
            print(f"{self.name} is already in perfect health!")

    def check_status(self):
        print(f"Pet Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
        print()

    def time_passes(self):
        self.hunger -= 5
        self.happiness -= 5
        self.health -= 5