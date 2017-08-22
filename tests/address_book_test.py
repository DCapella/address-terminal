import sys
sys.path.append("..")
from address_terminal.models.address_book import AddressBook
print("="*25,"\nSTART OF TESTS", "\n" + "="*25)

# start of tests
errors = 0

book = AddressBook()
print("Entries = 0")
print(len(book.entries) == 0)

book.add_entry('Jon Doe', '012.345.5789', 'jon.doe@email.com')
print("\nEntries = 1")
print(len(book.entries) == 1)

new_entry = book.entries[0]
print("\nName = 'Jon Doe'")
print(new_entry.name == "Jon Doe")

print("\nPhone Number = '012.345.5789'")
print(new_entry.phone_number == "012.345.5789")

print("\nEmail = 'jon.doe@email.com'")
print(new_entry.email == "jon.doe@email.com")

# end of tests
print("You have", errors, "error(s).")

print("="*25,"\nEND OF TESTS", "\n" + "="*25)
