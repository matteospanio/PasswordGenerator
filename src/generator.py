import string
import random # define the random module

# call random.choices() string module to find the string in Uppercase + numeric data.
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
print("The randomly generated string is : " + str(ran)) # print the random data


class StringGenerator:

    length:      int

    UPPERCASE:   str = string.ascii_uppercase
    LOWERCASE:   str = string.ascii_lowercase
    DIGITS:      str = string.digits
    SYMBOLS:     str = string.punctuation
    SAFE_SYMBLS: str = "!#$%&*+-=?@^_|"

    def __init__(self):
        # TODO
        self.ok = 1

    def generate() -> str:
        # TODO logic

        return "pwd"
            
