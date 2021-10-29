import string
import random

UPPERCASE:   str = string.ascii_uppercase
LOWERCASE:   str = string.ascii_lowercase
DIGITS:      str = string.digits
SYMBOLS:     str = string.punctuation
SAFE_SYMBLS: str = "!#$%&*+-=?@^_|"

class StringGenerator:

    length:     int
    uppercase:  bool
    lowercase:  bool
    digits:     bool
    symbols:    bool
    safe_symbls:bool


    def __init__(self, length,
                 uppercase, lowercase,
                 digits, symbols,
                 safe_symbls):
        self.uppercase  = uppercase
        self.lowercase  = lowercase
        self.digits     = digits
        self.symbols    = symbols
        self.safe_symbls= safe_symbls
        self.length     = length


    def generate(self) -> str:
        compose_string = (UPPERCASE if self.uppercase else "") +\
                         (LOWERCASE if self.lowercase else "") +\
                         (DIGITS    if self.digits    else "") +\
                         (SYMBOLS   if self.symbols   else "")

        ran = ''.join(random.choices(compose_string, k = self.length))
        return ran
            
