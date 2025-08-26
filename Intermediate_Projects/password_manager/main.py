from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():

    is_okay = messagebox.askokcancel(title=website_input.get(),
                                    message= f"These are the details entered:"
                                    f" \nEmail: {email_input.get()}"
                                    f" \nPasswordd: {password_input.get()}"
                                    f" \nIs it ok to save?")

    if is_okay:
        with open("data.txt", "a") as data:
            data.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")
        website_input.delete(0,END)
        password_input.delete(0, END)
        website_input.focus()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="ew")
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="ew")
email_input.insert(0, "marv4115@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="ew")

generate_button = Button(text="Generate Password", justify="left")
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")


window.mainloop()