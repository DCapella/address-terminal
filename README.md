# Address Terminal
A fun project creating a virtual address book coded with Python 3 and using terminal to work.

It is an application that can be used to store names with a phone number and email. You will be able to view, create, search and even import entries from a CSV.

Address Terminal was originally wrote in Ruby and I decided I wanted to see if I could change it over to Python. It was a lot of fun seeing how the different languages reacted.

Users need to be able to affect the entries by:

* Viewing
```Python
def view_all_entries(entry_name):
        """
        Allows you to view all the entries in the Address Book Object
        """
        for entry in self.address_book.entries:
            # system_clear()
            if entry.name >= entry_name:
                print("%s\n%s\n%s" % (entry.name, entry.phone_number, entry.email))
                entry_submenu(entry)

        system_clear()
        print("End of entries")
```

* Deleting
```Python
def delete_entry(entry):
        """Function to delete a selected entry"""
        system_clear()
        self.address_book.entries.remove(entry)
        print('%s has been deleted' % entry.name)
        view_all_entries(entry.name)
```

* Editing
```Python
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
```

* Creating
```Python
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
```

* Searching
```Python
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
```

* Importing
```Python
def import_from_csv(self, file_name):
      """
      Goes through each line of a csv file and adds entry
      """
      with open(file_name) as csvfile:
          reader = csv.reader(csvfile, delimiter=',')
          next(reader, None)
          for row in reader:
              self.add_entry(row[0], row[1], row[2])
```

* Exiting
```Python
def selection_5():
        """Selection 5 function that exits the terminal"""
        print("Good-bye!")
        exit(0)
```

Address Terminal features are tested in one file.

I decided to make my own tests only because I find it interesting.

```Python
book = AddressBook()

print("Entries = 0")
if len(book.entries) == 0:
    print("SUCCESS")
else:
    print("FAIL")
    errors += 1
```
![terminal-picture](address_terminal_tests.png)
