import os

# Function to save a message with a password
def save_message(message_file):
    # Set the password
    password = input("Set a password to save the message: ")

    # Save the password and messages to a file
    with open(message_file, 'w') as file:
        file.write(password + '\n')  # Save the password

        # Enter the message for correct password
        correct_message = input("Enter the message to display for correct password: ")
        file.write(correct_message + '\n')  # Save the correct message

        # Enter the message for wrong password
        wrong_message = input("Enter the message to display for wrong password: ")
        file.write(wrong_message)  # Save the wrong message

    print("\nMessages and password saved successfully.")
    print("Summary of saved data:")
    print(f"Password: {password}")
    print(f"Correct message: {correct_message}")
    print(f"Wrong message: {wrong_message}")

# Function to read the messages with a password
def read_message(message_file):
    if not os.path.exists(message_file):
        print("No saved message found.")
        return

    # Read the saved password and messages
    with open(message_file, 'r') as file:
        saved_password = file.readline().strip()  # Read the first line as the saved password
        correct_message = file.readline().strip()  # Read the second line as the correct message
        wrong_message = file.readline().strip()  # Read the third line as the wrong message

    # Ask for the password to read the message
    password_attempt = input("Enter the password to view the message: ")

    if password_attempt == saved_password:
        print("Your message is:", correct_message)
    else:
        print(wrong_message)

# Main function
def main():
    message_file = 'message.txt'

    while True:
        print("\nOptions:")
        print("1. Save a message")
        print("2. Read a message")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            save_message(message_file)
        elif choice == '2':
            read_message(message_file)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
