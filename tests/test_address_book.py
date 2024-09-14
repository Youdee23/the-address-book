from address_book import ContactInfo


def test_create_contact_info():
    """
    Assert that a contact info can be created with a firstname, a lastname
    and just one phone number
    """
    contact_info = ContactInfo("Alice", "Eti-mfon", "08023678079")

    assert contact_info.firstname == "Alice"
    assert contact_info.lastname == "Eti-mfon"
    assert contact_info.phonenumbers == ["08023678079"]


def test_add_phonenumber():
    """
    Asserts that phone number can be added to a contact info
    """ 
    contact_info = ContactInfo("Alice", "Eti-mfon", "08023678079")
    contact_info.add_phonenumber("08023678080")
    assert contact_info.phonenumbers == ["08023678079", "08023678080"]
    

def test_remove_phonenumber():
    """
    Asserts that phone number can be removed from contact info
    """
    contact_info = ContactInfo("Alice", "Eti-mfon", "08023678079")
    contact_info.remove_phonenumber("08023678079")
    assert contact_info.phonenumbers == []


def test_change_firstname():
    """
    Asserts that firstname can be changed
    """
    contact_info = ContactInfo("Alice", "Eti-mfon", "08023678079")
    contact_info.change_firstname("Uduak")
    assert contact_info.firstname == "Uduak"


def test_change_lastname():
    """
    Asserts that lastname can be changed
    """
    contact_info = ContactInfo("Alice", "Eti-mfon", "08023678079")
    contact_info.change_lastname("Udofia")
    assert contact_info.lastname == "Udofia"


def test_edit_phonenumber():
    """
    Asserts that phonenumber can be edited
    """
    contact_info = ContactInfo("Alice", "Eti-mfon", "08023678079")
    contact_info.edit_phonenumber("08012345678")
    assert contact_info.phonenumbers == ["08012345678"]
    
