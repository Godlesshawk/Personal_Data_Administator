import validators
import csv

person = ['name', 'lastname', 'day', 'month', 'year', 'age', 'postal code', 'address', 'city']


while True:
    value = input("Please choose which aspect to edit: (n)ame, (l)ast name, (d)ay of birth, (m)onth of birth, "
                  "(y)ear of birth (add)ress, (p)ostal code or (c)ity (enter 'q' to quit): ")

    match value.casefold():
        case 'n' | 'name':
            person[0] = validators.input_string("Please enter name (Enter 'q' to quit): ")
        case 'l' | 'lastname':
            person[1] = validators.input_string("Please enter your last name (Enter 'q' to quit): ")
        case 'd' | 'day':
            person[2] = validators.input_bounded_integer("Please enter the day of your birth (Enter 'q' to quit): ",
                                                   "Day of Birth", 1, 31)
        case 'm' | 'month':
            person[3] = validators.input_bounded_integer("Please enter the month of your birth (Enter 'q' to quit): ",
                                                   "Month of Birth", 1, 12)
        case 'y' | 'year':
            person[4] = validators.input_bounded_integer("Please enter the year of your birth (Enter 'q' to quit): ",
                                                   "Year of Birth", 0, 2022)
        case 'a' | 'age':
            person[5] = validators.input_bounded_integer("Please enter age (Enter 'q' to quit): ", "age", 0, 130)
        case 'p' | 'postal code':
            person[6] = validators.input_postal_code("Please enter postal code (Enter 'q' to quit): ",
                                               1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120,
                                               1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230)
        case 'add' | 'address':
            person[7] = validators.input_string("Please enter your address (Enter 'q' to quit): ")
        case 'c' | 'city':
            person[8] = validators.input_string("Please enter your city (Enter 'q' to quit): ")
        case 'Q' | 'q':
            with open('people.csv', 'w', newline='', encoding="UTF-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow(["Vorname", "Nachname", "Alter", "Adresse", "PLZ", "Ort"])
                writer.writerow([person[0], person[1], person[5], person[7], person[6], person[8]])
            quit(print('Vielen Dank für Ihren Besuch.'))



