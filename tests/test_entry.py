import sys
sys.path.append("..")
from address_terminal.address_terminal.entry import Entry
print("="*25,"\nSTART OF TESTS", "\n" + "="*25)

# start of tests
errors = 0

entry = Entry('name', '1234567890', 'email@email.com')

if entry.name != 'name':
    errors += 1
    print("Error: NAME")

if entry.phone_number != '1234567890':
    errors += 1
    print("Error: PHONE_NUMBER")

if entry.email != 'email@email.com':
    errors += 1
    print("Error: EMAIL")

# end of tests
print("You have", errors, "error(s).")

print("="*25,"\nEND OF TESTS", "\n" + "="*25)
