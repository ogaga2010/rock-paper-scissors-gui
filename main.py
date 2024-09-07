import random
import tkinter as tk
from tkinter import messagebox

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"
    
# Function to handle user's choice
def user_choice(choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = determine_winner(choice, computer_choice)
    messagebox.showinfo("Result", f"Your choice: {choice}\nComputer's choice: {computer_choice} \n\n{result}")

# Function to create the GUI
def create_gui():
    window = tk.Tk()
    window.title("Rock, Paper, Scissors Game")

    tk.Label(window, text="Choose Rock, Paper, or Scissors").pack()

    tk.Button(window, text="Rock", command=lambda: user_choice('Rock')).pack()
    tk.Button(window, text="Paper", command=lambda: user_choice('Paper')).pack()
    tk.Button(window, text="Scissors", command=lambda: user_choice('Scissors')).pack()

    window.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()