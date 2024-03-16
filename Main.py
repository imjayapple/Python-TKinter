import customtkinter

# Set Appearance and Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    username = input("Username: ")
    password = input("Password: ")

    # Assume we have a database of valid usernames & passwords
    valid_users = ["user1", "user2", "user3"]
    valid_passwords = ["pass1", "pass2", "pass3"]

    if username in valid_users and valid_passwords == valid_passwords[valid_users.index(username)]:
        print("Login Successful")
        # Add code here to redirect to the main application upon successful login
        
    else:
        print("Invalid username or password")
        # Add code to handle incorrect login attempts here

font = customtkinter.CTkFont(family="Arial", weight="normal", slant="italic")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()