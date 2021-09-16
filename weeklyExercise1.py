# PASSWORD VALIDATOR TEMPLATE: REPLACE THIS LINE WITH YOUR FILE HEADER

def validate(password):
    """ Analyzes an input password to determine if it is "Secure", "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters

    Returns:
        result (string): either "Secure", "Insecure", or "Invalid". 
    """
    # Invalid password criteria 
    forbiddenCharacters = " @#"
    minPassLength = 8

    # Secure password criteria
    secureCharacters = "!-$%&'()*+,./:;<=>?_[]^`{|}~"

    passwordInvalid = False
    passwordSecure = False

    if len(password) < minPassLength:
        passwordInvalid = True

    counter = 0
    while counter < len(password) and (not passwordInvalid):
        char = password[counter]

        if char in forbiddenCharacters:
            passwordStatus = "Invalid"
        else:
            pass

    if passwordInvalid:
        return "Invalid"

def generate(n):
    """ Generates a password of length n which is guaranteed to be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n. 
    """
    pass

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    validate("")

