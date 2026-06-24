🎮 Tic-Tac-Toe (Python/Tkinter)


A clean, interactive, and lightweight Tic-Tac-Toe game developed using Python and the tkinter library. This project provides a graphical interface for two players to compete in the classic game of strategy.


🚀 Features


Intuitive GUI: Built with tkinter for a responsive, desktop-based windowed experience.

Real-time Feedback: Automatically tracks whose turn it is and highlights the winning combination in green upon victory.

Input Validation: Prevents players from overriding existing moves.

Simple Logic: Uses a efficient checking system to validate all 8 possible winning combinations (rows, columns, and diagonals).


🛠️ Technologies Used

Language: Python 3.x

GUI Library: tkinter (Standard Python library)


🎮 How to Play

Clone the repository:

Bash
git clone https://github.com/nishantbhattgraphicgmailcom/Tic-Tac-Toe.git

Navigate to the folder:

Bash
cd Tic-Tac-Toe

Run the game:

Bash
python Tic-Tac-Toe.py

Players take turns clicking on any of the 9 empty cells to place an 'X' or an 'O'. The first player to align three marks in a row wins!


📜 How it Works

The game uses a list of 9 buttons initialized with a grid layout. The core logic relies on:

button_click(index): Validates move and updates the UI.

check_winner(): Iterates through winning combinations whenever a move is made.

toggle_player(): Manages the turn-based state between 'X' and 'O'.


Created by [Nishant Bhatt]


