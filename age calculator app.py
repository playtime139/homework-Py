from tkinter import *
from datetime import date

def calculate_age():
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    today = date.today()

    age = today.year - year

    if today.month < month or (today.month == month and today.day < day):
        age -= 1

    result_label.config(text="Your Age is: " + str(age))

root = Tk()
root.title("Age Calculator App")
root.geometry("300x250")

Label(root, text="Enter Day").pack()
day_entry = Entry(root)
day_entry.pack()

Label(root, text="Enter Month").pack()
month_entry = Entry(root)
month_entry.pack()

Label(root, text="Enter Year").pack()
year_entry = Entry(root)
year_entry.pack()

Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

result_label = Label(root, text="Your Age will appear here")
result_label.pack()

root.mainloop()