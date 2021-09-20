# PASSWORD VALIDATOR TEMPLATE: REPLACE THIS LINE WITH YOUR FILE HEADER

import random

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
    specialCharacters = "!-$%&'()*+,./:;<=>?_[]^`{|}~"
    
    secureAttributes = {"uppercase": False, "lowercase": False, 
                        "numbers": False, "specialChars": False}
    passwordInsecure = True
    generatedPw = ""

    while len(generatedPw) < n or passwordInsecure: 
        # Discard password if char limit reached and still insecure
        if len(generatedPw) >= n:
            for attribute in secureAttributes:
                secureAttributes[attribute] = False
            generatedPw = ""

        else:
            # Randomly pick symbol, letter, or number generation
            selection = random.randrange(0, 3)

            # Randomly select character
            if selection == 0:
                generatedPw += specialCharacters[random.randrange(0, len(specialCharacters))]
                secureAttributes["specialChars"] = True

            # Randomly select upper or lowercase letter
            elif selection == 1:
                letter = chr(random.randrange(97, 123))
                
                randCapitalize = random.randrange(0, 2)

                if randCapitalize:
                    generatedPw += letter.upper()
                    secureAttributes["uppercase"] = True
                else:
                    generatedPw += letter
                    secureAttributes["lowercase"] = True

            # Randomly select number
            else:
                generatedPw += chr(random.randrange(48, 58))
                secureAttributes["numbers"] = True

            # Check and set if password still insecure
            passwordInsecure = False
            for isSecure in secureAttributes.values():
                if isSecure:
                    pass
                else:
                    passwordInsecure = True
                    break

    return generatedPw





if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    print(generate(8))

