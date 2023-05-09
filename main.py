import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


def find_password():
    website = website_entry.get()
    try:

        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data found")
    else:
        if website in data:

            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email{email}\nPassword{password}")
        else:
            messagebox.showinfo(title="Error",message=f"No detail for {website} exists")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pasword():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.askokcancel(title="Oops",message="Please make sure you have not left any field empty")
    else:
         try:
             with open("data.json","r") as data_file:
                 #reading old data
                 data = json.load(data_file)
         except FileNotFoundError:
             with open("data.json","w") as data_file:
                 json.dump(new_data,data_file,indent=4)
         else:

             #updating old data with new data
             data.update(new_data)
             with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(new_data, data_file, indent=4)
         finally:

             website_entry.delete(0,tkinter.END)
             password_entry.delete(0,tkinter.END)





# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password manager")
window.config(pady=20,padx=50)

canvas = tkinter.Canvas(height=200,width=200)
logo_img = tkinter.PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(row=0,column=1)

website_label = tkinter.Label(text="Website")
website_label.grid(row=1)
email_label = tkinter.Label(text="Email/Username")
email_label.grid(row=2)
password_label = tkinter.Label(text ="Password")
password_label.grid(row=3)

#Entries

website_entry = tkinter.Entry(width=19)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"workbuzi1@gmail.com")
password_entry = tkinter.Entry(width=19)
password_entry.grid(row=3,column=1)


#buttons
generate_password_button = tkinter.Button(text="Generate Password",width=12,command=generate_pasword)
generate_password_button.grid(row=3,column=2)
add_button = tkinter.Button(text="Add",width=33,command=save)
add_button.grid(row=4,column=1,columnspan=2)
search_button = tkinter.Button(text="Search",width=12,command=find_password)
search_button.grid(row=1,column=2)


window.mainloop()


