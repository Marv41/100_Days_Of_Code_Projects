from tkinter import *

def calculate_km():
    miles = int(input_miles.get())
    km = miles * 1.60934
    result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400,height=100)
window.config(padx=10, pady=10)

input_miles = Entry()
input_miles.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to",padx=20)
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)


window.mainloop()







