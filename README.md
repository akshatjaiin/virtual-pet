# Virtual Pet Game

This project is a simple text-based virtual pet game implemented in Python. The player can interact with a virtual pet by feeding it, playing with it, and healing it. The game simulates the passage of time and includes random events that affect the pet's status.

## Table of Contents

- [Installation](#installation)
- [How to Play](#how-to-play)
- [Features](#features)
- [Project Structure](#project-structure)
- [System Requirements](#system-requirements)
- [License](#license)

## Installation

To run the game, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/akshatjaiin/virtual-pet-game.git
   cd virtual-pet-game
Run the Game: Make sure you have Python 3.x installed, then run the game using the following command:
python virtual_pet.py
No additional dependencies are required.

How to Play
Start the Game: You will be prompted to name your pet and specify its type (e.g., dog, cat, dragon, etc.).

Choose an Action: After the game starts, you will be presented with several options:

Feed: Increase your pet's hunger level.
Play: Increase your pet's happiness (but it decreases hunger).
Heal: Improve your pet's health.
Status: View your pet's current hunger, happiness, and health levels.
Quit: Exit the game.
Random Events: Occasionally, random events such as finding a toy (which increases happiness) or getting sick (which decreases health) will occur.

Game Over: If any of your pet's attributes (hunger, happiness, or health) reach 0, the game ends.

Features
Hunger, Happiness, and Health: The pet has three attributes that the player must manage:

Hunger: Increases when the pet is fed, decreases as time passes or during play.
Happiness: Increases when playing with the pet, decreases over time.
Health: Increases when healed, but may decrease due to random events.
Random Events:

The pet may randomly find a toy, increasing happiness.
The pet may randomly get sick, decreasing health.
Time Simulation: As the game progresses, the pet's attributes naturally decrease over time, creating a need for the player to maintain the pet's well-being.

Project Structure
plaintext
Copy code
├── virtual_pet.py       # Main game script
├── README.md            # Project documentation
System Requirements
Python 3.x
No additional dependencies or libraries are required to run this game.

License
This project is licensed under the MIT License. See the LICENSE file for details.


### Additional Notes:
- Make sure to save the script as `virtual_pet.py` in your project directory.
- Update the placeholder `git clone` URL with the actual repository URL if needed.

![image](https://github.com/user-attachments/assets/3c06debc-ca1b-4fd3-862e-cf31c9f4cd29)
