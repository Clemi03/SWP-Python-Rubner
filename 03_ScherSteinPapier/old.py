import tkinter as tk
import random

def play_rps(user_choice):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    result_string.set(f'You chose {user_choice} and the computer chose {computer_choice}.')
    if user_choice == computer_choice:
        result_string.set('It\'s a tie!')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        result_string.set('You win!')
    elif user_choice == 'paper' and computer_choice == 'rock':
        result_string.set('You win!')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        result_string.set('You win!')
    else:
        result_string.set('You lose.')

root = tk.Tk()
root.geometry("300x200")
root.title("Schere Stein Papier")

result_string = tk.StringVar()
result_label = tk.Label(root, textvariable=result_string)
result_label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: play_rps("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_rps("paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_rps("scissors"))
scissors_button.pack()

root.mainloop()
