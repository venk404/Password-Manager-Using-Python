import os.path
import random
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
# --- check data in file for the first-time --


# ---- Working Json ----
def save_json():
    new_data = {
        Website_Entry.get():
            {
                "email": Email_Entry.get(),
                "password": Password_Entry.get()
            }
    }
    try:  # if Try is true the only it will else run else exceot block will run false
        # read data from file
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
            messagebox.showinfo('Successfully', "Data as inserted in data.json")
    else:
        # update the data from old new
        data.update(new_data)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
            messagebox.showinfo('Successfully', "Data as inserted in data.json")
    finally:
        Website_Entry.delete(0, END)
        Password_Entry.delete(0, END)
        search_btn['state'] = NORMAL


# -------add line to csv file ------


# ---- saving Data in json or txt ---
def add():
    if validation_check():
        save_json()

    # file saving it in txt file
    # with open("website Creditionals.txt", "a") as f:
    #     f.write(f"Website:{Website_Entry.get()}| Email:{Email_Entry.get()}| Password:{Password_Entry.get()}\n")


# function for search button --
def search_website():
    website = Website_Entry.get()
    if len(website) > 0:
        with open("data.json") as file:
            dic_website = json.load(file)
            if website in dic_website:
                messagebox.showinfo(title=website,
                                    message=f"Email : {dic_website[website]['email']}\n\nPassword : {dic_website[website]['password']}")
            else:
                messagebox.showerror("Error", "Data not exists")
    else:
        messagebox.showinfo(title="INFO", message="Website cannot be empty to search")


# ------------------Password Mechianicm--------
def generate_password():
    Password_Entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = ""
    password_symbols = ""
    password_numbers = ""
    for i in range(0, 7):
        password_letters += random.choice(letters)
        if i < 5:
            password_symbols += random.choice(symbols)
            password_numbers += random.choice(numbers)
            password_numbers += random.choice(numbers)

    password_before_shuffle = list(password_numbers + password_letters + password_letters)
    shuffle(password_before_shuffle)
    password = "".join(password_before_shuffle)
    Password_Entry.insert(0, password)


# ---------------------UI-----------------
# # image
can = Canvas(height=200, width=200, highlightthickness=0)  # remove border
image = PhotoImage(file="logo.png")
can.create_image(100, 100, image=image)
can.grid(row=0, column=1)

# label
Website_label = Label(text="Website:", fg="black")
Website_label.grid(row=1, column=0)
Email_label = Label(text="Email/Username:", fg="black")
Email_label.grid(row=2, column=0)
Password_label = Label(text="Password:", fg="black")
Password_label.grid(row=3, column=0)

# textboxs
Website_Entry = Entry(width=32)
Website_Entry.grid(row=1, column=1)
Website_Entry.focus_set()

Email_Entry = Entry(width=50)
Email_Entry.grid(row=2, column=1, columnspan=2)

Email_Entry.insert(0, "abc@gmail.com")
Password_Entry = Entry(width=32)
Password_Entry.grid(row=3, column=1)

# buttons
search_btn = Button(text="Search", width=14, cursor="hand2", command=search_website, highlightthickness=0)
search_btn.grid(row=1, column=2)
Generate_password_btn = Button(text="Generate Password", width=14, command=generate_password, cursor="hand2")
Generate_password_btn.grid(row=3, column=2)
add_button = Button(text="Add", width=43, command=add, cursor="hand2")
add_button.grid(row=4, column=1, columnspan=2)


# validation for empty website textbox
def validation_check():
    if len(Website_Entry.get()) == 0:
        messagebox.showerror("error", 'The Website cannot be empty')
        return FALSE
    elif len(Email_Entry.get()) == 0:
        messagebox.showerror("error", "The Email cannot be empty")
        return FALSE
    elif len(Password_Entry.get()) == 0:
        messagebox.showerror("error", "The Password cannot be empty")
        return FALSE
    else:
        return TRUE


# file exists and file exists any content in it then only the search button
if os.path.isfile("data.json") != TRUE or os.path.getsize("data.json") <= 0:
    search_btn['state'] = "disabled"

window.mainloop()
