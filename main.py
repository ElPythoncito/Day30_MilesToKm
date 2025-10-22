# ---------------------------------------------- EL PYTHONCITO XD 🐍🐍🐍🐍!!!!
from tkinter import *
from tkinter import ttk, messagebox

FONT = ("Times new roman", 12)


# --------------------------------------------- Function
def calculate():
    try:
        value = float(miles_entry.get())

        if radio_state.get() == 1:
            miles_label.config(text="miles")
            km_label.config(text="km")
            km = round(value * 1.60934, 4)
            result_label.config(text=km)
        elif radio_state.get() == 2:
            miles_label.config(text="km")
            km_label.config(text="miles")
            miles = round(value / 1.60934, 4)
            result_label.config(text=miles)
        else:
            messagebox.showwarning("Warning ⚠️", "Please select a conversion option.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


# --------------------------------------------- Create the screen
window = Tk()
window.title("Day 30 Miles to km")
window.iconbitmap("./Logo.ico")
window.geometry("+800+300")
window.config(pady=20, padx=20)

# --------------------------------------------- Labels
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=4, sticky="e")

miles_label = Label(text="miles", font=FONT)
miles_label.grid(column=2, row=3)

km_label = Label(text="km", font=FONT)
km_label.grid(column=2, row=4)

result_label = Label(text="0", font=FONT, pady=10)
result_label.grid(column=1, row=4)

title = Label(text="El Pythoncito XD 🐍\nWhat conversion would you like to do?", font=("Times new roman", 14))
title.config(justify="center", pady=10)
title.grid(column=0, row=0, columnspan=3)

# ---------------------------------------- Entry
miles_entry = Entry()
miles_entry.config(justify="center", font=FONT, width=20)
miles_entry.grid(column=1, row=3)

# ----------------------------------------- Radiobutton
radio_state = IntVar()
radiobutton1 = ttk.Radiobutton(text="miles to km", value=1, variable=radio_state)
radiobutton2 = ttk.Radiobutton(text="km to miles", value=2, variable=radio_state)
radiobutton1.grid(column=0, row=1)
radiobutton2.grid(column=0, row=2)

# ----------------------------------------- Button
calculate_button = ttk.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=5)

# ----------------------------------
window.mainloop()
