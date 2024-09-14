class ContactInfo:
    def __init__(self, firstname, lastname, phonenumber):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumbers = [phonenumber]

    def add_phonenumber(self, phonenumber):
        self.phonenumbers.append(phonenumber)

    def remove_phonenumber(self, phonenumber):
        self.phonenumbers.remove(phonenumber)

    def change_firstname(self, firstname):
        self.firstname = firstname

    def change_lastname(self, lastname):
        self.lastname = lastname

    def edit_phonenumber(self, phonenumber):
        self.phonenumbers = [phonenumber]


    