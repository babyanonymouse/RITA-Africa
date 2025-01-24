# dependencies
import time
import json


# Load users data from file
def load_users():
    try:
        with open("user_database.json", "r") as file:
            data = file.read().strip()
            if not data:
                return {}
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Database file not found. Creating a new one...")
        with open("user_database.json", "w") as file:
            json.dump({}, tfile)  # Create an empty JSON object
        return {}


# Save user data to file
def save_users():
    global user_database
    with open("user_database.json", "w") as file:
        json.dump(user_database, file)


# Initialize user database
user_database = load_users()


# Function to register a user
def register_user():
    print("\n <-- REGISTER -->")
    # Prompt a username
    username = input("Enter a username: ").strip()
    if username in user_database:  # Check if username exists
        print("Username already exists! Try again.")
        return
    # Prompt password
    password = input("Enter your Password: ").strip()
    if len(password) < 6:
        print("Password can't be less than 6 characters!")  # Check if password is 6 chars or more
        return
    # Password confirmation
    confirm_password = input("Confirm your password: ").strip()
    if confirm_password != password:
        print("Passwords don't match!")
        return
    # Store the data in the dictionary
    user_database[username] = {"password": password}
    save_users()
    print("Registration Successful!")

# Function to login user
def login_user():


# Main Program Loop
while True:
    print("\n --- TaskFlow ---")
    time.sleep(1)  # delay timer
    print("Your Tasks, Your Flow, Your Success.")
    time.sleep(0.5)
    action = input("Choose an action (register/exit): ").strip().lower()
    if action == "register":
        register_user()
    elif action == "exit":
        print("Exiting the system ...")
        time.sleep(1)
        print("Bye")
        exit()
    else:
        print("Invalid action! Please choose 'register' or 'exit'")
