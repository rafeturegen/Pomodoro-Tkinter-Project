from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters)  for char in range(nr_letters)]
    symbols_list = [random.choice(symbols)  for char in range(nr_symbols)]
    numbers_list = [random.choice(numbers)  for char in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data, data_file, indent=4)
            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File Found")
    else:
        if website_entry.get() in data.keys():
            messagebox.showinfo(title=website_entry.get(), message=f"Email: {data[website_entry.get()]["email"]}"
                                                        f"\nPassword: {data[website_entry.get()]["password"]}")
        else:
            messagebox.showinfo(title="Error",message="No details for this website exists")
    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text="Search",width=14, command=find_password)
search_button.grid(row=1,column=2)

email_entry = Entry(width=50)
email_entry.insert(END, "rafetagaoyunda@hotmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
