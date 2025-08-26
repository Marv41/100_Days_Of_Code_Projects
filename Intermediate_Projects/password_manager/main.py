from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- SEARCH FEATURE ------------------------------- #
def search():
    website = website_input.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except JSONDecodeError:
        messagebox.showerror(title="Error", message="No Data File")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Existing Credentials Found\n"
                                                           f"Email: {email}\n"
                                                           f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} found")
        return True
    return False
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(0, randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(0, randint(2, 4))]
    number_list = [choice(numbers) for _ in range(0, randint(2, 4))]
    password_list = letters_list + symbols_list + number_list
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(END, password)
    pyperclip.copy(password)

    messagebox.showinfo("Password Generated", "Password saved to clipboard")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def check_empty():
    if not website_input.get() or not password_input.get():
        messagebox.showerror("Opps", "Please fill in the required fields.")
        return True
    else:
        return False

def add():
    new_data = {
        website_input.get(): {
            "email": email_input.get().title(),
            "password": password_input.get().title()
    }}
    if not check_empty() and not search():
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)

        except JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving the updated data
                json.dump(data, data_file, indent=4)

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
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="ew")
email_input.insert(0, "marv4115@gmail.com")

password_input = Entry(width=35)
password_input.grid(column=1, row=3)

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="ew")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()