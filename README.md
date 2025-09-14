# Rock Paper Scissors Web App

A simple web-based implementation of the classic Rock Paper Scissors game built with Flask.  
The game allows a user to decide how many rounds to play, records each round's outcome, and displays the final winner along with a round-by-round summary.

---

## Objective
- To practice building a Flask web application with session management.  
- To implement a turn-based game that tracks results across multiple rounds.  
- To design a clean, modern, and responsive user interface using Tailwind CSS.  
- To demonstrate how server-side state management can provide reliable gameplay without relying on client-side hacks.

---

## Features
- User selects the number of rounds before starting the game.  
- Turn-based gameplay where the user chooses Rock, Paper, or Scissors each round.  
- Random machine choice generated each round.  
- Server-side session tracking ensures game progress is saved reliably.  
- Final results show:
  - Total rounds played  
  - Number of wins, losses, and ties  
  - Round-by-round breakdown with user and machine choices  
- Responsive modern UI built with Tailwind CSS.  
- "Play Again" option to reset and start a new game.

---

## Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, Tailwind CSS (via CDN)  
- **State Management:** Flask Session  
- **Template Engine:** Jinja2 (Flask default)

---
### Live Demo Link:- https://stone-paper-scissor-game-q5hj.onrender.com

---

## Getting Started

### Prerequisites
- Python 3.8 or later  
- pip (Python package manager)  

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mahendra-jangid-ai/Stone-Paper-Scissor-Game.git
   cd flask-rock-paper-scissors

### Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows


### Install dependencies:
pip install -r requirements.txt


Run the Application
### python app.py

