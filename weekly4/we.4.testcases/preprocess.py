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


def preProcessWord(word):
    word = word.lower()
    processedWord = ""

    noSymbolWord = removeSymbols(word)

    if isStrNum(noSymbolWord):
        return noSymbolWord

    if isStopword(noSymbolWord):
        return ""

    for letter in word:
        if letter.isalpha():
            processedWord += letter

    return processedWord

def getWords():
    """"""
    strWords = input()
    return strWords.split()

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant 
    # to this exercise, so you should call your code from here.

    words = getWords()
    processedWordsList = []
    for word in words:
        processedWord = preProcessWord(word)

        if processedWord:
            processedWordsList.append(processedWord)

    processedWords = " ".join(processedWordsList)

    print(processedWords)
