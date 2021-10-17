#--------------------------------------------
#   Name: 
#   ID: 
#   CMPUT 274, Fall 2021
#
#   Weekly Exercise #4: Text Preprocessor
#-------------------------------------------- 

# NOTE:  Make sure all of your functions are properly documents
#   (e.g., with docstrings)

# You must determine how to structure your solution.
# Create your functions here and call them from under
# if __name__ == "__main__"!

import sys

def isStopword(word):
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
    return word.isnumeric()

def removeSymbols(word):
    noSymbolWord = ""

    for letter in word:
        if letter.isalpha() or letter.isnumeric():
            noSymbolWord += letter

    return noSymbolWord

def removeSingleNums(noSymbolWord):
    noNumWord = ""
    for letter in noSymbolWord:
        if not letter.isnumeric():
            noNumWord += letter

    return noNumWord


def preProcessWord(word, mode):
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
        return removeSingleNums(word)
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

def validMode():
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
    try:
        return sys.argv[1]
    except IndexError:
        return None



if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant 
    # to this exercise, so you should call your code from here.

    if not validMode():
        sys.exit()


    words = getWords()
    mode = getMode()
    processedWordsList = []
    for word in words:
        processedWord = preProcessWord(word, mode)

        if processedWord:
            processedWordsList.append(processedWord)

    processedWords = " ".join(processedWordsList)

    print(processedWords)
