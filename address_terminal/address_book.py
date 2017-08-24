from entry import Entry
import csv

class AddressBook(object):
    """
    Creating a new Address Book object
    """
    def __init__(self):
        """
        Inititalize object with attribute entries
        """
        self.entries = []

    def add_entry(self, name, phone_number, email):
        """
        Giving object the attribute to add entries
        """
        index = 0
        for item in self.entries:
            if name < item.name: break
            index += 1

        self.entries.insert(index, Entry(name, phone_number, email))

    def import_from_csv(self, file_name):
        """
        Goes through each line of a csv file and adds entry
        """
        with open(file_name) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)
            for row in reader:
                self.add_entry(row[0], row[1], row[2])
