class Employees():
    def __init__(self):
        self.FirstName = ''
        self.LastName = ''
        self.Address = ''

class DataScientists(Employees):
    def __init__(self):
        self.Programming = ''

ali = DataScientists()
ali.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ''

mar1 = Marketing()
mar1.


class Employees_yeni():
    def __init__(self, FirstName, LastName, Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address

ali = Employees_yeni('a', 'b', 'c')
ali.LastName
ali = Employees_yeni()   #TypeError
