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

def random_event(pet):
    event = random.choice(['find_toy', 'get_sick'])
    if event == 'find_toy':
        pet.happiness += 10
        print(f"{pet.name} found a toy and is happier!")
    elif event == 'get_sick':
        pet.health -= 20
        print(f"{pet.name} got sick!")
    

def game_loop():
    name = input("What do you want to name your pet? ").strip().lower()
    pet_type = input("What type of pet is it (dog, cat, dragon, etc.)? ")
    pet = Pet(name, pet_type)

    while True:
        print("\nWhat would you like to do?")
        action = input("Options: feed, play, heal, status, quit: ").strip().lower()

        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "heal":
            pet.heal()
        elif action == "status":
            pet.check_status()
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please choose again.")

        pet.time_passes()
        if random.random() < 0.3:
            random_event(pet)

        if pet.hunger <= 0 or pet.happiness <= 0 or pet.health <= 0:
            print(f"\n{pet.name} is in poor condition. Game over!")
            break

        time.sleep(1)

if __name__ == "__main__":
    game_loop()
