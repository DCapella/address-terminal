import sys
sys.path.append("..")
from address_terminal.address_terminal.entry import Entry

entry = Entry('name', '1234567890', 'email@email.com')

print(entry.name)
print(entry.phone_number)
print(entry.email)



import sys
sys.path.append("..")
from address_terminal.address_terminal.entry import Entry
print("="*25,"\nSTART OF TESTS", "\n" + "="*25)

# start of tests
errors = 0
# end of tests
print("You have", errors, "error(s).")

print("="*25,"\nEND OF TESTS", "\n" + "="*25)
