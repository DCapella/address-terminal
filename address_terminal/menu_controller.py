import os
from address_book import AddressBook

def system_clear():
    """
    Telling the terminal to clear the screen
    """
    absolutely_unused_variable = os.system("clear")

def get():
    """
    Getting input from the user
    """
    return input(">> ")

class MenuController(object):
    """
    Creating a new Menu Controller Object
    """
    def __init__(self, address_book = AddressBook()):
        """
        Inititalizing Menu Controller Object with attribute address_book
        """
        self.address_book = address_book

    def main_menu(self):
        """
        Main menu function that gives you the ability to go through, create,
        search, or import an entry in the Address Book
        """
        def view_all_entries():
            """
            Allows you to view all the entries in the Address Book Object
            """
            for entry in self.address_book.entries:
                system_clear()
                print(entry)
                entry_submenu(entry)

            system_clear()
            print("End of entries")

        def entry_submenu(entry):
            """
            Allows you to navigate while viewing all the entries in the Address
            Book Object
            """
            print("n - next entry")
            print("d - delete entry")
            print("e - edit this entry")
            print("m - return to main menu")

            selection = get()

            def get_selection(character, entry):
                """
                Reads your input and completes the necessary function
                """
                case_selection = {
                    'n': 'pass',
                    'd': 'pass',
                    'e': 'pass',
                    'm': 'pass'
                }

                if character not in case_selection:
                    system_clear()
                    print("Sorry,", character, "is not a valid input")
                    entry_submenu(entry)

                answer = case_selection.get(character, lambda: "nothing")
                return answer()

            get_selection(selection, entry)

        def create_entry():
            """
            Allows you to create a new entry for the Address Book Object
            """
            system_clear()
            print("New Address Entry")
            print("Name: ")
            name = get()
            print("Phone number: ")
            phone = get()
            print("Email: ")
            email = get()

            self.address_book.add_entry(name, phone, email)

            system_clear()
            print("New entry created")

        print("Main Menu -", len(self.address_book.entries), "entries")
        print("1 - View all entries")
        print("2 - Create an entry")
        print("3 - Search for an entry")
        print("4 - Import entries from a CSV")
        print("5 - Exit")
        print("Enter your selection: ")

        selection = input(">> ")

        def selection_1():
            """Selection 1 function that calls view_all_entries function"""
            system_clear()
            view_all_entries()
            self.main_menu()

        def selection_2():
            """Selection 2 function that calls create_entry function"""
            system_clear()
            create_entry()
            self.main_menu()

        def selection_3():
            """Selection 3 function that calls search_entries function"""
            system_clear()
            search_entries()
            self.main_menu()

        def selection_4():
            """Selection 4 function that calls read_csv function"""
            system_clear()
            read_csv()
            self.main_menu()

        def selection_5():
            """Selection 5 function that exits the terminal"""
            print("Good-bye!")
            exit(0)

        def get_selection(number):
            """
            Gets your input and calls the necessary function
            """
            case_selection = {
                '1': selection_1,
                '2': selection_2,
                '3': selection_3,
                '4': selection_4,
                '5': selection_5
            }

            if number not in case_selection:
                system_clear()
                print("Sorry that is not a valid input")
                self.main_menu()

            answer = case_selection.get(number, lambda: "nothing")
            return answer()

        get_selection(selection)
