# Game of Life

A Python implementation of Conway's Game of Life, a cellular automaton simulation that demonstrates how complex patterns can emerge from simple rules.

## Project Overview

This implementation features:
- Python-based console visualization
- Classic Game of Life rules:
  - Any live cell with fewer than two live neighbors dies (underpopulation)
  - Any live cell with two or three live neighbors lives on to the next generation
  - Any live cell with more than three live neighbors dies (overpopulation)
  - Any dead cell with exactly three live neighbors becomes a live cell (reproduction)

## Technical Details

The project is implemented in Python, using basic console output for visualization. It demonstrates fundamental programming concepts including:
- 2D array manipulation
- Cellular automata rules
- Console-based visualization
- Game loop implementation

## Project Context

This project was created as a test implementation to evaluate the effectiveness of Roo Code connected to Anthropic Claude 3.5 Sonnet 20241022-v2:0. It serves as a demonstration of:
- AI-assisted code development
- Version control workflow
- Project documentation practices
- Code organization and structure

## Requirements

- Python 3.6 or higher
- Dependencies are listed in `requirements.txt`:
  - pygame >= 2.0.0
  - numpy >= 1.19.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jayaustin/game-of-life.git
cd game-of-life
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Running the Game

To start the simulation:
```bash
python game_of_life.py
```

### Controls
- Click cells to toggle them between alive/dead
- Use the "Play/Pause" button to start/stop the simulation
- "Reset" button clears the grid
- "Randomize" button creates a random pattern

## Development Notes

This project was developed with assistance from Roo Code, an AI-powered development tool, using Anthropic's Claude 3.5 Sonnet model. The implementation process showcased the capabilities of AI-assisted development in:
- Project setup and organization
- Code implementation
- Documentation generation
- Version control integration
