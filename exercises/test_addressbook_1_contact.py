"""
Implement an Address Book.

It should include the following classes:

    - Contact: A single contact, with fields like: first, last, phone, email, address
    - Group: A group of contacts.
    - Addressbook: The entire address book. Can include contacts and groups.
"""

import pytest

from addressbook.contact import Contact, Picture

class TestContact(object):

    def test_fields(self):
        moshe = Contact(first="Moshe", last="Cohen")
        assert moshe.first == "Moshe"
        assert moshe.last == "Moshe"

        moshe.email = "moshe.cohen@gmail.com"
        moshe.address = "12 Jabotinsky st., Tel Aviv, Israel"
        moshe.phone = "03-1234567"
        moshe.picture = Picture("moshe.jpg")

    def test_contact_equality(self):
        contact1 = Contact(first="Moshe", last="Cohen")
        contact2 = Contact(first="David", last="Levy")
        contact3 = Contact(first="Moshe", last="Cohen")

        assert contact1 != contact2
        assert contact3 == contact1

    def test_contact_with_missing_arguments_raises(self):
        with pytest.raises(TypeError):
            Contact()

    def test_str(self):
        moshe = Contact(first="Moshe", last="Cohen")
        assert str(moshe) == "Moshe Cohen"

    def test_repr(self):
        moshe = Contact(first="Moshe", last="Cohen")
        assert repr(moshe) == "<Person 'Moshe Cohen'>"

    def test_properties(self):
        moshe = Contact(first="Moshe", last="Cohen")
        moshe.email = "moshe.cohen@gmail.com"

        assert moshe.full_name == "Moshe Cohen"
        assert moshe.full_email == "Moshe Cohen <moshe.cohen@gmail.com>"
