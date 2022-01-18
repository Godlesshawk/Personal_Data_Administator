import validators


while True:
    value = input("Please choose which aspect to edit: (a)ge, (h)eight, (p)ostalcode (or enter 'q' to quit): ")
    match value.casefold():
        case 'age' | 'a':
            print(validators.input_bounded_integer("Please enter age (Enter 'q' to quit): ", "age", 0, 130))
        case 'height' | 'h':
            print(validators.input_bounded_integer("Please enter height in centimeters (Enter 'q' to quit): ", "height", 20, 250))
        case 'postalcode' | 'p':
            print(validators.input_postal_code("Please enter postal code (Enter 'q' to quit): ", 1010, 1020, 1030, 1040, 1050, 1060, 1070))
        case 'Q' | 'q':
            quit(print('Vielen Dank für Ihren Besuch.'))




