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
                print("%s\n%s\n%s" % (entry.name, entry.phone_number, entry.email))
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
                    'd': delete_entry,
                    'e': edit_entry,
                    'm': 'pass'
                }

                if character not in case_selection:
                    system_clear()
                    print("Sorry,", character, "is not a valid input")
                    entry_submenu(entry)

                answer = case_selection.get(character, lambda: "nothing")
                return answer(entry)

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

        def read_csv():
            """Function to import entries from csv"""
            print("Enter CSV file to import: ")
            file_name = get()

            if not file_name:
                system_clear()
                print("No CSV file read")
                self.main_menu()

            try:
                self.address_book.import_from_csv(file_name)
                entry_count = self.address_book.count_csv(file_name)
                system_clear()
                print('%s new entries added from %s' % (entry_count, file_name))
            except Exception as e:
                system_clear()
                print(file_name + ' is not a valid CSV file, please enter the name of a valid CSV file')
                read_csv()

        def delete_entry(entry):
            """Function to delete a selected entry"""
            self.address_book.entries.delete(entry)
            print('%s has been deleted' % entry.name)

        def edit_entry(entry):
            """Function allowing user to update current entry"""
            system_clear()
            print("%s\n%s\n%s" % (entry.name, entry.phone_number, entry.email))
            print("Updated name: ")
            name = get()
            print("Updated phone number: ")
            phone_number = get()
            print("Updated email: ")
            email = get()

            if name: entry.name = name
            if phone_number: entry.phone_number = phone_number
            if email: entry.email = email

            system_clear()
            print("Updated entry: ")
            print("%s\n%s\n%s" % (entry.name, entry.phone_number, entry.email))
            entry_submenu(entry)

        def search_entries():
            """Function allowing user to search by name for an entry"""
            print("Search by name: ")
            name = get()
            match = self.address_book.binary_search(name)
            system_clear()
            if match != '':
                print("%s\n%s\n%s" % (match.name, match.phone_number, match.email))
            else:
                print("No match found for %s" % name)

        def search_submenu(entry):
            """
            A submenu function that allows user to delete, edit or return to
            main menu
            """
            print("d - delete entry")
            print("e - edit this entry")
            print("m - return main menu")

            def select_delete_entry():
                system_clear()
                delete_entry(entry)
                self.main_menu()

            def select_edit_entry():
                edit_entry(entry)
                system_clear()
                self.main_menu()

            def select_main_menu():
                system_clear()
                self.main_menu()

            selection = get()

            def get_selection(character, entry):
                """
                Reads your input and completes the necessary function
                """
                case_selection = {
                    'd': select_delete_entry,
                    'e': select_edit_entry,
                    'm': select_main_menu
                }

                if character not in case_selection:
                    system_clear()
                    print("Sorry,", character, "is not a valid input")
                    print("%s\n%s\n%s" % (entry.name, entry.phone_number, entry.email))
                    search_submenu(entry)

                answer = case_selection.get(character, lambda: "nothing")
                return answer()

            get_selection(selection, entry)

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
