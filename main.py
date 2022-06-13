from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    passwrd_input.delete(0, END)
    passwrd_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_input.get()
    email = email_username_input.get()
    passwrd = passwrd_input.get()

    if len(website) == 0 or len(email) == 0 or len(passwrd) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email : {email}\n "
                                                      f"Password : {passwrd}\n Is it ok to save?")
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{website} | {email} | {passwrd}\n")

            website_input.delete(0, END)
            # email_username_input.delete(0, END)
            passwrd_input.delete(0, END)
            website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="WebSite:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
passwrd_label = Label(text="Password:")
passwrd_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)
email_username_input = Entry(width=35)
email_username_input.insert(0, 'vismay@gmail.com')
email_username_input.grid(row=2, column=1, columnspan=2)
passwrd_input = Entry(width=21)
passwrd_input.grid(row=3, column=1)

generate_passwrd = Button(text="Generate Password", command=generate_password)
generate_passwrd.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
