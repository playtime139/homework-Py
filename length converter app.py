import tkinter as tk

def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result_label.config(text="Centimeters: " + str(cm))

window = tk.Tk()
window.title("Length Converter")

label = tk.Label(window, text="Enter length in inches:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Convert", command=convert)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()