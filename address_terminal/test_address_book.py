from address_book import AddressBook

def check_entry(entry, expected_name, expected_number, expected_email):
    if entry.name == expected_name and entry.phone_number == expected_number and entry.email == expected_email:
        return True
    else:
        return False


# start of tests
print("="*25 + "\nSTART OF TESTS" + "\n" + "="*25)
errors = 0

book = AddressBook()

print("Entries = 0")
if len(book.entries) == 0:
    print("SUCCESS")
else:
    print("FAIL")
    errors += 1

print("\nEntries = 1")
book.add_entry('Jon Doe', '012.345.5789', 'jon.doe@email.com')
if len(book.entries) == 1:
    print("SUCCESS")
else:
    print("FAIL")
    errors += 1

print("\nCheck entry name, phone number, and email")
new_entry = book.entries[0]
if check_entry(new_entry, 'Jon Doe', '012.345.5789', 'jon.doe@email.com'):
    print("SUCCESS")
else:
    print("FAIL")
    errors += 1

book_csv = AddressBook()

print("\nImport from csv, entries == 5")
book_csv.import_from_csv("entries.csv")
if len(book_csv.entries) == 5:
    print("SUCCESS")
else:
    print("FAIL")
    errors += 1

print("\nChecks the 1st entry")
# book_csv.import_from_csv("entries.csv")
entry_one = book_csv.entries[0]
if check_entry(entry_one, 'aFirst', '123.456.7890', 'first@first.com'):
    print("SUCCESS")
else:
    print("FAIL")
    errors += 1

print("\nChecks the 2nd entry")
# book_csv.import_from_csv("entries.csv")
entry_two = book_csv.entries[1]
if check_entry(entry_two, 'bSecond', '234.567.8901', 'second@second.com'):
    print("SUCCESS")
else:
    print("FAIL")
    errors += 1

print("\nChecks the 3rd entry")
# book_csv.import_from_csv("entries.csv")
entry_three = book_csv.entries[2]
if check_entry(entry_three, 'cThird', '345.678.9012', 'third@third.com'):
    print("SUCCESS")
else:
    print("FAIL")
    errors += 1

print("\nChecks the 4th entry")
# book_csv.import_from_csv("entries.csv")
entry_four = book_csv.entries[3]
if check_entry(entry_four, 'dFourth', '456.789.0123', 'fourth@fourth.com'):
    print("SUCCESS")
else:
    print("FAIL")
    errors += 1

print("\nChecks the 5th entry")
# book_csv.import_from_csv("entries.csv")
entry_five = book_csv.entries[4]
if check_entry(entry_five, 'eFifth', '567.890.1234', 'fifth@fifth.com'):
    print("SUCCESS")
else:
    print("FAIL")
    errors += 1

# end of tests
print("\nYou have " + str(errors) + " error(s).")
print("="*25 + "\nEND OF TESTS" + "\n" + "="*25)
