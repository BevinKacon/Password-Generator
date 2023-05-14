import random
import string
from breezypythongui import EasyFrame

class PasswordGenerator(EasyFrame):
    """
    A GUI application for generating and storing passwords.
    
    Made by Gabriel Seaburn.
    """
    def __init__(self):
        """
        Initialize the PasswordGenerator class.
        """
        EasyFrame.__init__(self, title="Password Generator", width=300, height=150)
        self.addLabel(text="Password Length", row=0, column=0)
        self.lengthField = self.addIntegerField(value=0, row=0, column=1)
        self.addButton(text="Generate", row=3, column=0, columnspan=2, command=self.generate_password)
        self.addButton(text="View Passwords", row=4, column=0, columnspan=2, command=self.view_passwords)
        self.addButton(text="Exit Program", row=5, column=0, columnspan=2, command=self.exit_program)
        
        self.passwords = []  # List to store generated passwords

    def generate_password(self):
        """
        Generate a password based on the specified length and display it in a message box.
        """
        try:
            selected_length = self.lengthField.getNumber()  # Get the selected length from the GUI field
            characters = string.ascii_letters + string.digits + string.punctuation

            if selected_length > 11:
                random_password = ''.join(random.choice(characters) for i in range(selected_length))

                self.save_password(random_password)  # Save the password to a file
                self.passwords.append(random_password)  # Add the password to the list

                self.messageBox(title="Generated Password", message=random_password)
            else:
                self.messageBox(title="Error", message="You must have a length of at least 12 characters!")
        except ValueError:
            self.messageBox(title="Error", message="You have to input an integer!")

    def save_password(self, password):
        """
        Save the generated password to a file.
        """
        file_path = "passwords.txt"  # Specify the file path to save the passwords
        with open(file_path, "a") as file:
            file.write(password + "\n")

    def view_passwords(self):
        """
        Display the stored passwords from the file in a message box.
        """
        file_path = "passwords.txt"
        with open(file_path, "r") as file:
            opened_file = file.read()
        self.messageBox(title="Stored Passwords", message=opened_file)

    def exit_program(self):
        """
        Exit the program.
        """
        exit()

PasswordGenerator().mainloop()








