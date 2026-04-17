class Contact:
    def __init__(self, nameList, phoneNumber, email, birthday):
        """
        Variables Sent:
            Name, Phone number, Email, Birthdate

        Create Instance variables:
            - First Name:   first
            - Middle Name:  middle
            - Last Name:    last
            - Phone Number: mobile
            - Email:        email
            - BirthDate:    birthdate
        """
        self.first = nameList[0]
        if len(nameList) == 3:
            self.middle = nameList[1]
            self.last = nameList[2]
        else:
            self.middle = ""
            self.last = nameList[1]
        self.mobile = phoneNumber
        self.email = email
        self.birthdate = birthday

    def getName(self):
        """
        Return the name as a string like this "first middle last"
        The middle name might not exist
        """
        if self.middle:
            return f"{self.first} {self.middle} {self.last}"
        else:
            return f"{self.first} {self.last}"

        

    def __str__(self):
        """
        Returns a string representing the contact:
        > Contact: Josh Baker - (3178675309)
        """
        return f"Contact: {self.getName()} - ({self.mobile})"
    
    def __repr__(self):
        """
        Provided: 
        - Feel free to read more about it here: https://stackoverflow.com/questions/1436703/difference-between-str-and-repr
        """
        return self.__str__() # This is provided. Helps with something printing a list of contact items. 

    def call(self):
        """
        Simulate calling the contact.
        1. Print "Dialing <first name> ..."
        2. They don't pick up, so prompt the user to input a voicemail message
        3. Print the message that was entered
        """
        print(f"Dialing {self.first}...")
        message = input("Leave a voicemail: ")
        print(message)


    def sendText(self, message):
        """
        Send a text message to the contact.
        Print the recipient's first name and the message in this format:
        > To <first name>:
        >     <message>
        """
        print(f"To {self.first}: ")
        print(f"\t{message}")

    def sendBirthdayText(self):
        """
        Send a pre-written birthday message to the contact.
        Use sendText() to send the message — it handles the printing for you!
        The message should include the contact's first name.
        """
        self.sendText(f"Happy Birthday {self.first}!")

    def updateNumber(self, phoneNumber):
        """
        Take in a new phone number and replace the user's current phone number
        """
        self.mobile = phoneNumber
