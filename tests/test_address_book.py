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
    