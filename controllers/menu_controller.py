import sys
sys.path.append("..")
from address_terminal.models.address_book import AddressBook

class MenuController(object):
    def __init__(self, address_book = AddressBook()):
        self.address_book = address_book

    def main_menu:
        print("Main Menu -", len(address_book.entries), "entries")
        print("1 - View all entries")
        print("2 - Create an entry")
        print("3 - Search for an entry")
        print("4 - Import entries from a CSV")
        print("5 - Exit")
        print("Enter your selection: ")

        selection = input(">> ")
        print("You picked", selection)
