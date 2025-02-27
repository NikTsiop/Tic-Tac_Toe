# Tic-Tac-Toe with Minimax AI

## Overview
This is a command-line Tic-Tac-Toe game implemented in Python. It supports both **Player vs. Player** and **Player vs. AI** modes. The AI is powered by the **Minimax algorithm**, allowing it to make optimal moves.

## Features
- **Play against another player** or **challenge the AI**.
- **AI uses Minimax** for optimal move selection.
- **Dynamic board printing** for an interactive gameplay experience.
- **Detects win conditions (rows, columns, diagonals) and draws.**
- **Custom player names and symbols.**

## Installation
### **Requirements**
This project runs on Python **3.x** and does not require external dependencies.

### **Clone the Repository**
```bash
git clone https://github.com/your-repository/tic-tac-toe.git
cd tic-tac-toe
```

### **Run the Game**
```bash
python tic_tac_toe.py
```

## How to Play
1. **Select game mode:**
   - (1) Player vs. Player
   - (2) Player vs. Computer
2. **Enter player names and symbols (optional).**
3. **Take turns placing marks on the board.**
4. **Win by getting 3 in a row, column, or diagonal.**
5. **If the board is full with no winner, it's a draw.**

## Minimax AI Explanation
- The **Minimax algorithm** evaluates all possible moves and selects the best one.
- AI assigns **+10 for a win**, **-10 for a loss**, and **0 for a draw**.
- The depth factor helps the AI prioritize faster victories and avoid delays.
- The AI will **always try to win** or **block a player's winning move**.

## Example Game Flow
```
Player 0 (X) vs. Player 1 (O)

 X |   | O
-----------
   | X |   
-----------
 O |   | X  

Player 0 is the winner!
```

## Future Improvements
- Add a GUI using Tkinter or Pygame.
- Implement an Alpha-Beta pruning optimization for Minimax.
- Extend board size (e.g., 4x4 or 5x5 support).

## License
This project is open-source and available under the **MIT License**.

## Author
Developed by NikTsiop

