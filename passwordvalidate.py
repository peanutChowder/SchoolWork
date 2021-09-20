# PASSWORD VALIDATOR TEMPLATE: REPLACE THIS LINE WITH YOUR FILE HEADER

def validate(password):
    """ Analyzes an input password to determine if it is "Secure", "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters

    Returns:
        result (string): either "Secure", "Insecure", or "Invalid". 
    """
    invalidCharacters = " @#"
    validLength = 8 
    specialCharacters = "!-$%&'()*+,./:;<=>?_[]^`{|}~"
    
    secureAttributes = {"uppercase": False, "lowercase": False, 
                        "numbers": False, "specialChars": False}

    passwordStatus = "Insecure"

    # Check for sufficient length
    if len(password) < validLength:
        passwordStatus = "Invalid"

    # Check the validity and security of each character
    charCounter = 0
    while passwordStatus != "Invalid" and charCounter < len(password):
        char = password[charCounter]

        if char in invalidCharacters:
            passwordStatus = "Invalid"
        else:
            if char in specialCharacters:
                secureAttributes["specialChars"] = True
            elif char.isnumeric():
                secureAttributes["numbers"] = True
            elif char.isupper():
                secureAttributes["uppercase"] = True
            else:
                secureAttributes["lowercase"] = True

        charCounter += 1

    # Exit function if password invalid
    if passwordStatus == "Invalid":
        return passwordStatus

    # Check if password secure or insecure
    passwordStatus = "Secure"
    for isSecure in secureAttributes.values():
        if isSecure:
            pass
        else:
            passwordStatus = "Insecure"
            break

    return passwordStatus

    

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
    print(validate("helloworld!"))

