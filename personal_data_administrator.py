import validators
import csv

class Person:
    def __init__(self):
        self.name = None
        self.lastname = None
        self.day = None
        self.month = None
        self.year = None
        self.age = None
        self.postalcode = None
        self.address = None
        self.city = None


class CsvWriter:
    def write(self, person: Person):
        with open('people.csv', 'w', newline='', encoding="UTF-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(["Vorname", "Nachname", "Alter", "Adresse", "PLZ", "Ort"])
            writer.writerow([x.name, x.lastname, x.age, x.address, x.postalcode, x.city])
        
    def read(self) -> Person:

        pass

x = Person()
y = CsvWriter()


while True:
    value = input("Please choose which aspect to edit: (n)ame, (a)ge, (l)ast name, (d)ay of birth, (m)onth of birth, "
                  "(y)ear of birth (add)ress, (p)ostal code or (c)ity (enter 'q' to quit): ")
    
    match value.casefold():
        case 'n' | 'name':
            x.name = validators.input_string("Please enter name (Enter 'q' to quit): ")
        case 'l' | 'lastname':
            x.lastname = validators.input_string("Please enter your last name (Enter 'q' to quit): ")
        case 'd' | 'day':
            x.day = validators.input_bounded_integer("Please enter the day of your birth (Enter 'q' to quit): ",
                                                   "Day of Birth", 1, 31)
        case 'm' | 'month':
            x.month = validators.input_bounded_integer("Please enter the month of your birth (Enter 'q' to quit): ",
                                                   "Month of Birth", 1, 12)
        case 'y' | 'year':
            x.year = validators.input_bounded_integer("Please enter the year of your birth (Enter 'q' to quit): ",
                                                   "Year of Birth", 0, 2022)
        case 'a' | 'age':
            x.age = validators.input_bounded_integer("Please enter age (Enter 'q' to quit): ", "age", 0, 130)
        case 'p' | 'postal code' | 'postalcode':
            x.postalcode = validators.input_postal_code("Please enter postal code (Enter 'q' to quit): ",
                                               1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120,
                                               1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230)
        case 'add' | 'address':
            x.address = validators.input_string("Please enter your address (Enter 'q' to quit): ")
        case 'c' | 'city':
            x.city = validators.input_string("Please enter your city (Enter 'q' to quit): ")
        case 'Q' | 'q':
            y.write(x)
            quit(print('Vielen Dank für Ihren Besuch.'))

