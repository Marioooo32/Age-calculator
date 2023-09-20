import tkinter as tk
from datetime import date

def calculate_age():
    today = date.today()
    birth_date = date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    age_label.config(text=f"Your age is: {age}")

root = tk.Tk()
root.title("DarkGPT Age Calculator")

# Year Entry
year_label = tk.Label(root, text="Enter your birth year:")
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack()

# Month Entry
month_label = tk.Label(root, text="Enter your birth month:")
month_label.pack()
month_entry = tk.Entry(root)
month_entry.pack()

# Day Entry
day_label = tk.Label(root, text="Enter your birth day:")
day_label.pack()
day_entry = tk.Entry(root)
day_entry.pack()

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_age)
calculate_button.pack()

# Age Label
age_label = tk.Label(root, text="")
age_label.pack()

root.mainloop()