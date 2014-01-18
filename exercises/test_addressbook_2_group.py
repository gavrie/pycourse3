"""
Implement an Address Book.

It should include the following classes:

    - Contact: A single contact, with fields like: first, last, phone, email, address
    - Group: A group of contacts.
    - Addressbook: The entire address book. Can include contacts and groups.
"""

from addressbook.contact import Contact
from addressbook.group import Group


class TestGroup(object):

    def test_group(self):
        tamar = Contact(first="Tamar", last="Givon")
        sarah = Contact(first="Sarah", last="Cohen")
        david = Contact(first="David", last="Levy")

        group = Group()
        group.add(tamar)
        group.add(sarah)

        assert len(group) == 2

        assert tamar in group
        assert sarah in group
        assert david not in group
