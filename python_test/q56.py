# Define the correct password
password = "password123"

# Prompt the user to enter a password
user_input = input("Enter password: ")

# Keep prompting until correct password is entered
while user_input != password:
    print("Incorrect password!")
    user_input = input("Enter password: ")

print("Correct password!")