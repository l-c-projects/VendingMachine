import pandas as pd
import tkinter as tk
from tkinter import ttk
import hashlib
from datetime import date
from cryptography.fernet import Fernet


df = pd.read_csv("passwords.txt", delimiter=",")

#print(df)


#THIS ADDS ROWS TO THE DF
#I need to make sure I have some kind of text entry and button
#populate these variables
def add_entry(client,computer,user,password,date_added):
    password = password
    df.loc[len(df)] = [client,computer,user,password,date_added]
    df.to_csv("passwords.txt", index=False)

def add_entry_button():
    date_added = date.now()
    add_entry(add_client_entry.get(),add_computer_entry.get(),add_user_entry.get(),add_password_entry.get(),add_date_added)

#THIS IS TO MAKE THE ACTUAL PASSWORD FILE
def make_password_file(client_for_file):
    client_df = df.loc[(df['Client'] == client_for_file)]

    client_file_name = f"{client_for_file}.txt"

    client_df.to_csv(client_file_name, index=False)

def make_password_file_button(client_for_file):
    make_password_file(client_for_file)

#this is just so i can raise the dispenser frame easier
def raise_dispenser_frame():
    dispener_frame.tkraise()

#update this later to use bcrypt because this is insecure.
def compare_pass_to_hash():
    user_pass_input = password_entry.get()
    # user_pass_input would be made by the login screen
    storage_hash = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08" 
    #CHANGE THIS

    #now i need to decrypt all passwords

    master_hash = hashlib.sha256(user_pass_input.encode()).hexdigest()
    print("Pass Input: ", user_pass_input)
    print("Generated Hash: ", master_hash)
    print("Stored Hash: ", storage_hash)
    if master_hash == storage_hash:
        raise_dispenser_frame()
        #so right here would be where i decrypt the password column

    else:
        error_label.config(text="Invalid Master Password")
        #so right here would be where i decrypt the password column

def generate_combobox_options():
    client_options = df["Client"]

def on_close():
    print("Saving data...")
    # save df, encrypt data once again using key.
    window.destroy()

def search_df():
    new_df = df[df["Client"].str.contains(lookup_client_entry.get(), case=False, na=False)
            & df["Computer"].str.contains(lookup_computer_entry.get())]

    lookup_results_box.delete("1.0", tk.END)
    lookup_results_box.insert(tk.END, new_df.to_string(index=False))
#if lookup_client_entry.get() == "":


    #lookup_computer_entry
    #lookup_password_entry_disp
    #lookup_user_entry"""
    

    
#this is where i am gooing to make a custom pandas search using the inputs of 
#all of the lookup_entry 

    

 #this is for testing the writing to the passwords.txt
#add_entry(client,computer,user,password,date_added)
#print(df)



#okay so let's get organized we are going to need
#1. a way to encrypt the client password column
    #A. so my current theory is that w
    #compares it to the already stored password hashenever the application opens,
    #then you input a password and it hashes the password thenh.
    
#2. a way to add that information, likely a few drop downs and text DONE
#fillouts on a dedicated tab DONE
    #A. so just make tkinter buttons and then have it use add_entry() DONE

#3.a way to write that information onto a sticky on command.
#I think my make_password_file fill this need DONE

#4.a way to put in a client name and shoot out add_entry()
    #A. also put in the options so that you can put in all and it gives you everything

#5. okay so i need to make a viewing window during lookup so that as they search
#they can see results then i need a button to shoot out the results of the search
#onto a note

###########################################################
#FRAME CREATION
###########################################################

#region FRAME CREATION
window = tk.Tk()

window.title("Login")
window.geometry('800x800')
window.configure(bg='white')
window.protocol("WM_DELETE_WINDOW", on_close)

container = tk.Frame(window)
container.pack(fill="both", expand=True)
container.configure(bg="white")

login_frame = tk.Frame(container, bg="white")
dispener_frame = tk.Frame(container, bg="white")



for frame in (login_frame, dispener_frame):
    frame.grid(row=0, column=0, sticky="nsew")
    frame.configure(bg="white")
#endregion
######################################################################
#LOGIN FRAME
########################################################################
#region LOGIN FRAME
#login widgets
login_label=tk.Label(login_frame, text="Enter the Master Password",  bg="#333333",
                     fg="#FFFFFF", font=("Aria", 14))
#username_label = tk.Label(login_frame, text="Username")
#username_entry = tk.Entry(login_frame)
password_entry = tk.Entry(login_frame, show="*",bg="white")
password_label = tk.Label(login_frame, text='Password', bg="white")
login_button = tk.Button(login_frame, text="Login", bg="red", fg="white",
                         font=("Aria", 14), command=compare_pass_to_hash)
error_label = tk.Label(login_frame)


error_label.grid(row=3, column=0,columnspan=2)
login_label.grid(row=0, column=0, columnspan=2, sticky="news")
#username_label.grid(row=1, column=0)
#username_entry.grid(row=1, column=1)
password_label.grid(row=1, column=0, pady=10)
password_entry.grid(row=1, column=1, pady=10)
login_button.grid(row=2, column =0, columnspan=2)

#endregion
#####################################################################
# DISPENSER FRAME START
########################################################################
#region DISPENSER FRAME
#dispenser widgets

# Labels (Row 2)
add_client_label = tk.Label(dispener_frame, text="Client")
add_computer_label = tk.Label(dispener_frame, text="Computer")
add_user_label = tk.Label(dispener_frame, text="User")
add_password_label_disp = tk.Label(dispener_frame, text="Password")

# Inputs (Row 3)
add_client_entry = ttk.Combobox(
    dispener_frame,
    values=df["Client"].unique().tolist()
)

add_computer_entry = tk.Entry(dispener_frame)
add_user_entry = tk.Entry(dispener_frame)
add_password_entry_disp = tk.Entry(dispener_frame)

# Place Labels
add_client_label.grid(row=2, column=1, padx=5, pady=5)
add_computer_label.grid(row=2, column=2, padx=5, pady=5)
add_user_label.grid(row=2, column=3, padx=5, pady=5)
add_password_label_disp.grid(row=2, column=4, padx=5, pady=5)

# Place Inputs
add_client_entry.grid(row=3, column=1, padx=5, pady=5)
add_computer_entry.grid(row=3, column=2, padx=5, pady=5)
add_user_entry.grid(row=3, column=3, padx=5, pady=5)
add_password_entry_disp.grid(row=3, column=4, padx=5, pady=5)


create_entry_button = tk.Button(dispener_frame, text= "Submit", bg="red", fg="white",
                         font=("Aria", 14), command=add_entry_button)

create_entry_button.grid(row=2, column=5, padx=5, pady=5, rowspan=2)

add_entry_label = tk.Label(dispener_frame, text="Add an Entry", font=("Aria", 14))
add_entry_label.grid(row=2, column=0, padx=5, pady=5, rowspan=2)








#endregion
#############################################################
#LOOKUP
################################################################
#region CLIENT LOOKUP
#dispenser widgets

# Labels (Row 1)
lookup_client_label = tk.Label(dispener_frame, text="Client")
lookup_computer_label = tk.Label(dispener_frame, text="Computer")
lookup_user_label = tk.Label(dispener_frame, text="User")
lookup_password_label_disp = tk.Label(dispener_frame, text="Password")

# Inputs (Row 2)
lookup_client_entry = ttk.Combobox(
    dispener_frame,
    values=df["Client"].unique().tolist()
)

lookup_computer_entry = tk.Entry(dispener_frame)
lookup_user_entry = tk.Entry(dispener_frame)
lookup_password_entry_disp = tk.Entry(dispener_frame)

# Place Labels
lookup_client_label.grid(row=5, column=1, padx=5, pady=5)
lookup_computer_label.grid(row=5, column=2, padx=5, pady=5)
lookup_user_label.grid(row=5, column=3, padx=5, pady=5)
lookup_password_label_disp.grid(row=5, column=4, padx=5, pady=5)

# Place Inputs
lookup_client_entry.grid(row=6, column=1, padx=5, pady=5)
lookup_computer_entry.grid(row=6, column=2, padx=5, pady=5)
lookup_user_entry.grid(row=6, column=3, padx=5, pady=5)
lookup_password_entry_disp.grid(row=6, column=4, padx=5, pady=5)

lookup_results_box = tk.Text(dispener_frame, height=15,width=80, bg="gray", fg="lightgray")
lookup_results_box.grid(row=4,column=0,columnspan=5,)

results_lookup_scrollbar = tk.Scrollbar(dispener_frame, command=lookup_results_box.yview)

lookup_results_box.config(yscrollcommand=results_lookup_scrollbar.set)

lookup_button = tk.Button(dispener_frame, text= "Submit", bg="red", fg="white",
                         font=("Aria", 14), command=search_df)

create_entry_button.grid(row=6, column=5, padx=5, pady=5, rowspan=2)

search_entries_label = tk.Label(dispener_frame, text="Search Entries", font=("Aria", 14))
search_entries_label.grid(row=6, column=0, padx=5, pady=5, rowspan=2)

#This is the button that will start the note making process
create_note_button = tk.Button(dispener_frame, text= "Create Note", bg="red", fg="white",
                         font=("Aria", 14), command=make_password_file)

create_note_button.grid(row=8, column=2, padx=10, pady=5, rowspan=3)


#endregion

login_frame.tkraise()
window.mainloop()


