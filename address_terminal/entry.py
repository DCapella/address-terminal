class Entry(object):
    """
    Creating a new Entry object for the Address Book
    """
    def __init__(self, name, phone_number, email):
        """
        Initializing Entry object with attributes name, phone_number, and email
        """
        self.name         = name
        self.phone_number = phone_number
        self.email        = email
