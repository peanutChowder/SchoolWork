#--------------------------------------------
#   Name: Jacob Feng
#   ID: 1591656
#   CMPUT 274, Fall 2021
#
#   Weekly Exercise #4: Text Preprocessor
#-------------------------------------------- 

import sys

def isStopword(word):
    """ Returns bool of whether the given string parameter is a stopword. Note that the parameter must be in lowercase.

    Arguments:
        word (str): lowercase string of the word to check

    Returns:
        (boolean): bool value of whether the word is a stopword
    """
    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
        "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", 
        "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", 
        "themselves", "what", "which","who", "whom", "this", "that", "these", "those", 
        "am", "is", "are", "was", "were", "be","been", "being", "have", "has", "had", 
        "having", "do", "does", "did", "doing", "a", "an","the", "and", "but", "if", 
        "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", 
        "about", "against", "between", "into", "through", "during", "before", "after", 
        "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
        "under", "again", "further", "then", "once", "here", "there", "when", "where", 
        "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", 
        "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", 
        "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    return word in stopwords

def isStrNum(word):
    """ Returns bool of whether the given string is fully composed of numeric digits.

    Arguments:
        word (str): string of the word to check

    Returns:
        (boolean): bool value of whether the string is only numeric digits"""
    return word.isnumeric()

def removeSymbols(word):
    """ Removes symbolic characters from a given string.

    Arguments:
        word (str): string of the word to remove symbols from

    Returns:
        noSymbolWord (str): new string of the given word without symbols
    """
    noSymbolWord = ""

    for letter in word:
        if letter.isalpha() or letter.isnumeric():
            noSymbolWord += letter

    return noSymbolWord

def removeNums(word):
    """ Removes all numeric digits from the given string.

    Arguments:
        word (str): string of the word to remove numeric digits from

    Returns:
        noNumWord (str): new string of the original word without numeric digits
    """
    noNumWord = ""
    for letter in word:
        if not letter.isnumeric():
            noNumWord += letter

    return noNumWord


def preProcessWord(word, mode):
    """ Performs preprocessing on a given word. When no mode is given, all symbols, stopwords, and numeric digits are removed
    (unless the string is only composed of numeric digits). Symbol, stopword, and numeric digits can be turned off one at a time 
    via the mode parameter. Note that the mode parameter must match a string literal exactly (i.e. case sensitive).

    Arguments:
        word (str): string of the word to perform preprocessing on
        mode (str): string of the specific preprocessing mode to use

    Returns:
        word (str): string of the preprocessed word or an empty string if the given word argument is a stopword and keep-stops mode
                    is not selected
    """
    # Turn all chars to lowercase in word if possible
    word = word.lower()

    # Remove symbol chars if keep-symbols mode off
    if mode != "keep-symbols":
        word = removeSymbols(word)

    # Return entire token if completely composed of numbers
    if isStrNum(word):
        return word

    # Return empty str if keep-symbols mode off and str is stopword
    if mode != "keep-stops" and isStopword(word):
        return ""

    # Remove all numbers from word if keep-digits mode is off
    if mode != "keep-digits":
        return removeNums(word)
    else:
        return word

def getWords():
    """ Takes a one line input of space delimited tokens (words) and returns the tokens in a list without spaces.

    Arguments:
        none

    Returns:
        (list): List of inputted tokens with no spaces
    """
    strWords = input()
    return strWords.split()

def isValidMode():
    """ Check if the user inputted command line mode is an existing mode. Returns bool of whether mode is a valid mode. 
    Returns False and prints error message if mode is not found within modes list.

    Arguments:
        none

    Returns:
        (bool): bool of whether the selected mode is valid
    """
    modes = ["keep-digits", "keep-stops", "keep-symbols"]
    modesStr = ", ".join(modes)
    
    try:
        if sys.argv[1] not in modes:
            print("Error: Invalid mode selected.")
            print(f"Try: 'python3 preprocess.py [mode]', where mode is one of {modesStr}.")
            return False

    except IndexError:
        return True

    else:
        return True

def getMode():
    """ Returns the command line mode. Returns empty string if no command line mode was inputted.

    Arguments:
        none

    Returns:
        (str): String of command line mode. If no mode specified, returns empty string.
    """
    try:
        return sys.argv[1]
    except IndexError:
        return ""



if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant 
    # to this exercise, so you should call your code from here.

    # If user selected option is not valid exit program
    if not isValidMode():
        sys.exit()

    # Get inputted words and given mode
    words = getWords()
    mode = getMode()
    processedWordsList = []

    # Perform preprocessing on words one by one
    for word in words:
        processedWord = preProcessWord(word, mode)

        # Add preprocessed word to the list if it is not empty string
        if processedWord:
            processedWordsList.append(processedWord)

    # Output preprocessing results
    processedWords = " ".join(processedWordsList)
    print(processedWords)
