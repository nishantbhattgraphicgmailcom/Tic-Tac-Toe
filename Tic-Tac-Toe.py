import tkinter as tk
from tkinter import messagebox

# This function checks all 8 winning combinations in Tic-Tac-Toe
def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        # Check if the three buttons in a winning combo have the same non-empty text
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight the winning buttons in green
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            # Show a winner alert and close the game
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

# Handles what happens when a player clicks a button
def button_click(index):
    # Only update if the button is empty and no one has won yet
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()  # Check if this move won the game
        toggle_player() # Switch turn to the other player

# Switches between Player X and Player O
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Initialize the main GUI window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create a list of 9 buttons for the grid
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

# Place buttons in a 3x3 grid layout
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Initialize game state variables
current_player = "X"
winner = False

# Create the label that displays whose turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start the game loop
root.mainloop()