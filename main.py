import tkinter as tk
from tkinter import messagebox
# import csv
import json
import pyperclip
from password_generator import password_generator


def generate_password():
    password = password_generator()
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)


def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "emile": username,
            "password": password,
        }
    }

    if len(website) <= 0 or len(username) <= 0 or len(password) <= 0:
        if len(website) == 0:
            messagebox.showerror(title="Password Manager", message="Website entry cannot be empty!")
        elif len(username) == 0:
            messagebox.showerror(title="Password Manager", message="Email/Username entry cannot be empty!")
        elif len(password) == 0:
            messagebox.showerror(title="Password Manager", message="Password entry cannot be empty!")

    elif messagebox.askyesno(title="Password Manager",
                             message=f"These are the detail entered:\nWebsite: {website}\nEmail/Username: {username}"
                             f"\nPassword: {password}"):

        # header = ["website", "email/username", "password"]
        # data = [website, username, password]
        # check_header = 0
        # with open("password_manager_data.csv", "r") as file:
        #     reader = csv.reader(file)
        #     for row in reader:
        #         if row == header:
        #             check_header = 1
        #             break
        #
        # with open("password_manager_data.csv", "a", newline="") as file:
        #     writer = csv.writer(file)
        #     if check_header != 1:
        #         writer.writerow(header)
        #     writer.writerow(data)

        try:
            with open("password_manager_data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("password_manager_data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("password_manager_data.json", "w") as file:
                json.dump(data, file, indent=4)


def search():
    check = 0
    website = website_entry.get()

    if len(website) <= 0:
        messagebox.showerror(title="Password Manager", message="Email/Username entry cannot be empty!")
    else:
        username_entry.delete(0, "end")
        password_entry.delete(0, "end")

        try:
            with open("password_manager_data.json", "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    if key == website:
                        username_entry.insert(0, data[key]["emile"])
                        password_entry.insert(0, data[key]["password"])
                        check = 1
                        break

                if check == 0:
                    messagebox.showerror(title="Password Manager", message="Website not found!")
        except FileNotFoundError:
            messagebox.showerror(title="Password Manager", message="Data file is empty!")


def clear():
    if messagebox.askyesno(title="Password Manager", message="Do you want to clear entries?"):
        website_entry.delete(0, "end")
        username_entry.delete(0, "end")
        password_entry.delete(0, "end")


white = "#FFFFFF"
black = "#000000"

root = tk.Tk()
root.minsize(width=750, height=400)
root.title("Password Manager")

image = tk.PhotoImage(file="padlock_image.png")

canvas = tk.Canvas(width=750, height=400, bg=white)
canvas.place(x=0, y=0)
canvas.create_image(285, 90, image=image)

title = tk.Label(text="Password\nManager", font=("Arial", 36, "bold"), fg=black, bg=white, justify="left")
title.place(x=345, y=57.5)

website_title = tk.Label(text="Website:", font=("Arial", 18, "normal"), fg=black, bg=white)
website_title.place(x=95, y=200)

website_entry = tk.Entry(width=28)
website_entry.place(x=245, y=200)
website_entry.focus()

search_button = tk.Button(text="Search", font=("Arial", 16, "normal"), bd=1, fg=black, bg=white, width=15,
                          command=search)
search_button.place(x=520, y=200)

username_title = tk.Label(text="Email/Username:", font=("Arial", 18, "normal"), fg=black, bg=white)
username_title.place(x=60, y=250)

username_entry = tk.Entry(width=48)
username_entry.place(x=245, y=250)

password_title = tk.Label(text="Password:", font=("Arial", 18, "normal"), fg=black, bg=white)
password_title.place(x=90, y=300)

password_entry = tk.Entry(width=28)
password_entry.place(x=245, y=300)

generate_button = tk.Button(text="Generate Password", font=("Arial", 16, "normal"), bd=1, fg=black, bg=white, width=15,
                            command=generate_password)
generate_button.place(x=520, y=300)

add_button = tk.Button(text="Add Password", font=("Arial", 16, "normal"), bd=1, fg=black, bg=white, width=20,
                       command=add_password)
add_button.place(x=244.5, y=350)

clear_button = tk.Button(text="Clear", font=("Arial", 16, "normal"), bd=1, fg=black, bg=white, width=20, command=clear)
clear_button.place(x=475, y=350)

root.mainloop()
