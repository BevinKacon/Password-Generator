from breezypythongui import EasyFrame
import random
import string


def generatePassword(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    generatedPasswords = set()

    try:
        length = int(input("Please input the length of the password you are wanting to generate: "))
        amountOfPasswords = int(input("Please input the amount of passwords you would like to generate: "))
        if length >= 8:
            for i in range(amountOfPasswords):
                password = generatePassword(length)
                print("Your password is:", password)

        else:
            print("You must have a password of at least 8 characters!")

    except ValueError:
        print("You must enter a valid number!")

    while True:
        password = ''.join(random.choice(characters) for i in range(length))
        
        if password not in generatedPasswords:
            generatedPasswords.add(password)
            return password
    



class EmptyWindow(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Password Generator", width = 300, height = 150)
        self.addLabel(text = "Password Length", row = 0, column = 0)
        self.lengthField = self.addIntegerField(value = 0, row = 0, column = 1)
        self.addButton(text = "Generate", row = 3, column = 0, columnspan = 2, command = generatePassword(length))
EmptyWindow().mainloop()





