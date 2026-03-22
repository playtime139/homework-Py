import tkinter as tk
import random

def play(user):
    comp = random.choice(["Rock", "Paper", "Scissors"])
    
    if user == comp:
        result = "Draw"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissors" and comp == "Paper"):
        result = "Win"
    else:
        result = "Lose"
    
    label.config(text=f"You: {user} | Computer: {comp} → {result}")

root = tk.Tk()

tk.Button(root, text="Rock", command=lambda: play("Rock")).pack()
tk.Button(root, text="Paper", command=lambda: play("Paper")).pack()
tk.Button(root, text="Scissors", command=lambda: play("Scissors")).pack()

label = tk.Label(root)
label.pack()

root.mainloop()