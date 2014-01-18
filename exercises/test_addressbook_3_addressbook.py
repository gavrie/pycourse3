"""
Implement an Address Book.

It should include the following classes:

    - Contact: A single contact, with fields like: first, last, phone, email, address
    - Group: A group of contacts.
    - Addressbook: The entire address book. Can include contacts and groups.
"""

from addressbook.contact import Contact
from addressbook.group import Group
from addressbook import Addressbook


class TestAddressbook(object):

    def test_addressbook(self):
        book = Addressbook()

        moshe = Contact(first="Moshe", last="Cohen")
        david = Contact(first="David", last="Levy")

        assert len(book) == 0

        book.add(moshe)
        book.add(david)
        assert len(book) == 2

        book.add(moshe)
        assert len(book) == 3

    def test_groups(self):
        book = Addressbook()

        tamar = Contact(first="Tamar", last="Givon")
        david = Contact(first="David", last="Levy")

        group1 = Group()
        group2 = Group()

        group1.add(tamar)

        book.add(group1)
        book.add(group2)

        group2.add(david)

        # Test
        assert tamar in group1
        assert david in group2

        assert tamar not in group2
        assert david not in group1

        assert tamar in book
        assert david in book

        group1.add(david)
        assert david in group1
        assert david in group2

        group1.remove(david)
        assert david not in group1


    def test_search(self):

        # Setup
        book = Addressbook()

        moshe = Contact(first="Moshe", last="Cohen")
        tamar = Contact(first="Tamar", last="Givon")
        sarah = Contact(first="Sarah", last="Cohen")
        david = Contact(first="David", last="Levy")

        moshe.phone = "03-1234567"

        book.add(moshe)
        book.add(tamar)
        book.add(sarah)

        # Check status
        assert moshe in book
        assert tamar in book
        assert sarah in book
        assert david not in book

        # Search
        results = book.search("mosh")
        assert len(results) == 1
        assert moshe in results

        results = book.search("cohen")
        assert len(results) == 2
        assert sarah in results
        assert moshe in results

        assert moshe in book.search("1234567")
        assert tamar not in book.search("foo")

        # Remove
        book.remove(tamar)
        assert tamar not in book
        assert len(book) == 2
