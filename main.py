from tkinter import *

window = Tk()
window.title("Mile to Km convertor")


def convert():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result.config(text=km)


miles_input = Entry(width=8)
miles_input.grid(column=2, row=0)
miles_label = Label(text="miles")
miles_label.grid(column=3, row=0)

is_equal_to = Label(text="is equal to ")
is_equal_to.grid(column=1, row=2)

kilometer_result = Label(text=0)

kilometer_result.grid(column=2, row=2)

kilometer_label = Label(text="label")
kilometer_label.grid(column=2, row=3)

calculate_button = Button(text='Calculate',command=convert)
calculate_button.grid(column=2, row=3)

window.mainloop()
