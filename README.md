# Island Height Finder
A Python game where players must find the highest island on a map through strategic guessing.
The game features a topographical map with islands of varying heights, challenging players to use visual cues and deduction to locate the highest elevation.
## 🎮 Game Description
In Island Height Finder, players are presented with a map containing multiple islands with different elevation levels. 
The goal is to identify the island with the highest elevation within a limited number of guesses. 
Each guess that isn't the highest island gets "flooded" (turns into water), preventing repeat guesses and adding strategic depth to the gameplay.
## Features

- Fetch map data from a provided URL
- Render the grid of cells based on their height values
- Allow the user to click on an island and display its average height
- Determine the correct island with the greatest average height
- Keep track of the user's guesses and the game state (won, lost, number of guesses remaining)
- Display the game state information on the screen
- Height legend for easy reference
- Implement game over and restart functionality

## 🛠️ Installation

1. Clone the repository:

```bash 
git clone https://github.com/jmarko02/Island_Height_Finder.git
```
2. Install the required dependencies:
```bash
pip install pygame numpy requests
```
3. Run the game:
```bash
python main.py
```

## 🎯 How to Play

Start the game by running main.py

You have 3 guesses to find the highest island

Click on an island to make a guess

If wrong:

The selected island turns into water
You lose one guess


If correct:

You win the game!


Press ESC or click the X button to exit

Use the restart button to play again

## 🎨 Color Guide
Height ranges are indicated by different colors:

0: Water (Blue)

1-150: Beach (Sand)

151-300: Lowland (Light Green)

301-450: Forest (Dark Green)

451-600: High Forest (Forest Green)

601-800: Mountain (Brown)

801-1000: Peak (Grey)

## 🎮 Controls

Left Mouse Click: Select an island

ESC: Exit game

Restart Button: Start new game (appears after win/loss)

Exit Button: Close game (appears after win/loss)

## 📁 Project Structure
```angular2html
island_height_finder/
│
├── main.py          # Game entry point
├── game.py          # Main game logic
├── map.py           # Map generation and island detection
├── config.py        # Game settings and constants
│
└── assets/          # Game assets (images)
    ├── sea.png
    ├── sand.png
    ├── grass.png
    └── ...
```

## 🛠️ Technical Details

Written in Python using Pygame

Uses NumPy for efficient array operations

Fetches map data from an external API

Implements flood fill algorithm for island detection

Features responsive UI with game state management

## 🔄 Game States

"playing": Active gameplay

"won": Player found highest island

"lost": Used all guesses without finding highest island

"quit": Game exit

## 🐛 Known Issues

Window resizing not currently supported

API dependency for map generation

## 🔮 Future Improvements

Difficulty levels

Custom map sizes

Score tracking

Animations

Sound effects

Multiplayer mode

Tutorial system

Statistics tracking

## 🙏 Acknowledgments

Nordeus for the challenge and API

Pygame community for resources and documentation