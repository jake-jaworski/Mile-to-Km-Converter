from tkinter import *


def conversion():
    user_input = float(entry.get())
    answer = user_input * 1.609
    output["text"] = f"{answer}"


# initialize the app window
window = Tk()
window.title("Miles to Kilometers Converter")
# window.minsize(height=200, width=400)
window.config(padx=20, pady=20)

# initialize calculate button
calculate = Button()
calculate.config(text="Calculate", command=conversion)

# initialize user entry field
entry = Entry(width=10, font=("Arial", 16, "normal"), )
entry.insert(END, string="0")

# initialize labels
miles = Label(text="Miles (mi)", font=("Arial", 16, "normal"))
equal_to = Label(text="is equal to", font=("Arial", 16, "normal"))
km = Label(text="kilometers (km)", font=("Arial", 16, "normal"))
output = Label(text="0", font=("Arial", 16, "normal"))

# set objects locations
equal_to.grid(column=0, row=1)
entry.grid(column=1, row=0)
output.grid(column=1, row=1)
calculate.grid(column=1, row=2)
miles.grid(column=2, row=0)
km.grid(column=2, row=1)


window.mainloop()