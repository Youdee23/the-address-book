class ContactInfo:
    def __init__(self, firstname, lastname, phonenumber):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumbers = [phonenumber]

    def add_phonenumber(self, phonenumber):
        self.phonenumbers.append(phonenumber)

    
        