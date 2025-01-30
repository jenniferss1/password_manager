from tkinter import *
from tkinter import messagebox

# PASSWORD GENERATOR


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) <= 0 and len(password) <= 0:
        messagebox.showinfo(title="Empty fields", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"f" Email: {email}\n"
                                                              f" Password: {password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password} \n\n")
                # clear the inputs fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)  # Centraliza a logo sobre as 3 colunas

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "jennifer@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky="ew")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

# Configuração das colunas para centralizar
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()