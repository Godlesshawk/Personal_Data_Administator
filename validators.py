def input_postal_code(prompt, *postalcodes):
    while True:
        value = input(prompt)

        if value.casefold() == 'q':
            return None

        try:
            return _check_postalcode(value, postalcodes)
        except ValueError as error:
            print(error)


def _concatenate(postalcodes):
    return ", ".join(str(code) for code in postalcodes)


def _check_postalcode(value, postalcodes):
    while True:
        try:
            postalcode = int(value)
        except ValueError:
            raise ValueError(f"Please enter a valid postalcode, e.g., {_concatenate(postalcodes)}. Your input '{value}' "
                             f"was not numerical.")

        if postalcode not in postalcodes:
            raise ValueError(f"Please enter a valid postal code, your input {postalcode} is not in the valid postal code "
                             f"list {_concatenate(postalcodes)}")

        return postalcode


def input_bounded_integer(prompt, description, minimum, maximum):
    while True:
        value = input(prompt)

        if value.casefold() == 'q':
            return None

        try:
            return _check_bounded_integer(int(value), description, minimum, maximum)
        except ValueError as error:
            print(error)


def _check_bounded_integer(value, description, minimum, maximum):
    while True:
        if not type(value) is int:
            raise TypeError(f"Please enter a valid age, your input {value} is not acceptable.")

        if value > maximum:
            raise ValueError(f"Please enter a valid age, your input {value} is not between {minimum} and {maximum}.")
        elif value < minimum:
            raise ValueError(f"Please enter a valid age, your input {value} is not between {minimum} and {maximum}.")

        return value