import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Enter a password")
    elif length < 5:
        result_label.config(text="Weak Password", fg="red")
    elif length < 8:
        result_label.config(text="Medium Password", fg="orange")
    else:
        result_label.config(text="Strong Password", fg="green")

window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("300x200")

tk.Label(window, text="Enter Password:").pack(pady=5)

entry = tk.Entry(window, show="*")
entry.pack(pady=5)

tk.Button(window, text="Check Strength", command=check_strength).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()