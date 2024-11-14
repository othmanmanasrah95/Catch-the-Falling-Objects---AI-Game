# Catch the Falling Objects Game

A simple game built using Python and `pygame`. The objective is to catch falling objects to increase your score.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [How to Run the Game](#how-to-run-the-game)
- [How to Play](#how-to-play)
- [Gameplay](#gameplay)
- [Customization](#customization)
- [License](#license)

## Overview

This game is a beginner-friendly project using Python and the `pygame` library. It involves controlling a player rectangle at the bottom of the screen to catch falling objects. The game increases in difficulty as the objects fall faster over time.

## Installation

### Prerequisites

1. **Python**: Make sure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Pygame**: The game requires the `pygame` library, which is a library designed for writing games in Python.

### Step-by-Step Installation

1. **Install Python**:
   - Visit [python.org](https://www.python.org/) and download Python 3.x for your operating system.
   - Follow the installation instructions for your OS (Windows, Mac, or Linux).
   - Verify the installation by typing the following command in your terminal or command prompt:
     ```bash
     python --version
     ```

2. **Install Pygame**:
   - Once Python is installed, open a terminal or command prompt and install `pygame` with the following command:
     ```bash
     pip install pygame
     ```

3. **Verify Pygame Installation**:
   - You can verify if `pygame` is installed by running:
     ```bash
     python -m pygame.examples.aliens
     ```
   - If a game window opens, `pygame` is successfully installed.

## How to Run the Game

1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the directory where the game file is saved.
3. Run the game by executing the following command:

   ```bash
   python catch_the_falling_objects.py
## How to Play

- **Objective**: Catch as many falling red objects as possible to increase your score.
- **Controls**:
  - Use the **left arrow key** to move left.
  - Use the **right arrow key** to move right.
  
Position the player (blue rectangle) under the falling object (red square) to catch it. Each successful catch increases your score by 1 point.

## Gameplay

- The game starts with one object falling from a random position at the top of the screen.
- When you catch an object, the score increments, and the object's speed increases, making the game more challenging.
- If an object falls past the bottom of the screen, it resets and falls again from the top.
- The game can be exited by closing the game window.

## Customization

You can easily customize various aspects of the game in the code:

- **Object Speed**: Increase or decrease the initial `object_speed` variable to make the game easier or harder.
- **Player Size and Speed**: Modify the `player_width`, `player_height`, or `player_speed` variables to change the player’s size or movement speed.
- **Colors**: Change the RGB values in the `white`, `black`, `red`, and `blue` variables to use different colors for the background, player, and object.
