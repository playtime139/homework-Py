import tkinter as tk

def calculate():
    try:
        P = float(principal_entry.get())
        R = float(rate_entry.get())
        T = float(time_entry.get())

        # Simple Interest
        SI = (P * R * T) / 100

        # Compound Interest
        CI = P * (1 + R/100) ** T - P

        result_label.config(
            text=f"Simple Interest: {SI:.2f}\nCompound Interest: {CI:.2f}"
        )

    except:
        result_label.config(text="Enter valid numbers")

# GUI
window = tk.Tk()
window.title("Interest Calculator")
window.geometry("350x300")

tk.Label(window, text="Principal Amount").pack()
principal_entry = tk.Entry(window)
principal_entry.pack()

tk.Label(window, text="Rate of Interest (%)").pack()
rate_entry = tk.Entry(window)
rate_entry.pack()

tk.Label(window, text="Time (years)").pack()
time_entry = tk.Entry(window)
time_entry.pack()

tk.Button(window, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()