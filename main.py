import json
import tkinter
from tkinter import *
from tkinter import messagebox
import csv
import password_generator
import pyperclip


def find_password():
     website = entry_website.get()
     try:
        with open("password_file.json", "r") as data_file:
            data = json.load(data_file)
     except FileNotFoundError:
        gen_json()
        with open("password_file.json", "r") as data_file:
            data = json.load(data_file)

     if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=f"{website}", message=f"Your login details for {website} are:\nEmail:  {email}\nPassword:  {password}")
     else:
        messagebox.showinfo(title="Error", message=f"There are no login detail stored for {website}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen_entry():
    new_password = password_generator.pass_gen()
    entry_password.delete(0, 'end')
    entry_password.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def gen_json():
    with open("password_file.json", "w") as new_file:
        blank_data = {}
        json.dump(blank_data, new_file)

def gen_dict():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if entry_website.get() == "" or entry_password.get() == "":
        messagebox.showinfo(title="Empty Field", message="You cannot leave fields blank")
    else:
        try:
            with open("password_file.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            gen_json()
            with open("password_file.json", "r") as data_file:
                 data = json.load(data_file)
                 data.update(new_data)
        finally:
            with open("password_file.json", "w") as data_file:
                 json.dump(data, data_file, indent=4)

        entry_website.delete(0, 'end')
        entry_password.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1, columnspan=2)

label_website = Label(text="Website:", font=("Tahoma", 10))
label_website.grid(column=1, row=2)

label_email = Label(text="Email/Username:", font=("Tahoma", 10))
label_email.grid(column=1, row=3)

label_password = Label(text="Password:", font=("Tahoma", 10))
label_password.grid(column=1, row=4)

entry_website = Entry(width=32)
entry_website.focus()
entry_website.grid(column=2, row=2, columnspan=2, sticky="w")

entry_email = Entry(width=40)
entry_email.insert(0, string="techno-trousers@hotmail.com")
entry_email.grid(column=2, row=3, columnspan=2, sticky="w")

entry_password = Entry(width=21)
entry_password.grid(column=2, row=4, sticky="w")

button_gen = Button(text="Generate Password", command=pass_gen_entry)
button_gen.grid(column=3, row=4, sticky="w")

button_add = Button(text="Add", width=33, command=gen_dict)
button_add.grid(column=2, row=5, columnspan=2, sticky="w")

button_search = Button(text="Search", command=find_password)
button_search.grid(column=3, row=2, sticky="e")

window.mainloop()
