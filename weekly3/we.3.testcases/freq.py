#--------------------------------------------
#   Name: Jacob Feng
#   ID: 1591656
#   CMPUT 274
#
#   Weekly Exercise 3: Word Frequency
#-------------------------------------------- 

import sys


def correctArgNum():
    """ Verifies that the freq.py file is called with exactly 2 arguments. Returns True if called with 2 arguments, otherwise returns False. Additionally prints to stdout whether
    the user called the file with too many or too little arguments.

    Arguments:
        none

    Returns:
        (bool): either True or False
    """
    if len(sys.argv) > 2:
        print("Too many arguments. Usage: python3 freq.py <input_file_name>")
        return False

    elif len(sys.argv) < 2:
        print("Too few arguments. Usage: python3 freq.py <input_file_name>")
        return False

    else:
        return True


def getFileContents():
    """ Verifies that the freq.py file is called with the correct number of arguments as well as checking that the provided file name could be opened successfully. If file opens 
    successfully, returns the split ontents of the file as a list, where splitting occurs wherever there is whitespace between characters. If an exception is raised during opening,
    the program is exited. 

    Arguments:
        none

    Returns:
        contentList (list): List of a file's contents split by whitespace 
    """
    if not correctArgNum():
        sys.exit()

    try:
        file = open(sys.argv[1], "r")
    except:
        print("File does not exist. Try again.")
    else:
        contentList = file.read().split()
        return contentList


def getWordFrequency(contentList):
    """ Counts the occurrences of each word when given a list of words. Additionally calculates the ratio of each word's occurrences with respect to the total word count.
    Returns a dictionary with a string representation of each unique word (case-sensitive) as keys and a list containing occurences and occurrence ratio as the values.

    Arguments:
        contentList (list): List of a file's contents split by whitespace 

    Returns:
        freqDict (dict): Dictionary containing a file's words as keys and a list of respective word occurrences and a 0 int as the values
    """
    freqDict = {}
    wordCount = len(contentList)

    for word in contentList:
        # Create key value pair for word if it does not already exist
        if word not in freqDict:
            freqDict[word] = [1, 0]

        # Increment by one if word already exists as a key
        else:
            freqDict[word][0] += 1

    setFrequencyRatio(freqDict, wordCount)
    return freqDict


def writeFreq(freqDict):
    """ Writes the results of a file word frequency analysis to a file with the given filename suffixed with '.out'. Results are written as follows: [word] [occurrences] [occurrence ratio].

    Arguments: 
        freqDict (dict): Dictionary containing a file's words as keys and a list of respective word occurrences and occurrence ratios as the values

    Returns:
        none
    """
    file = open(sys.argv[1] + ".out", "w")

    alphabeticalKeys = sorted(freqDict.keys())

    # Write stats for each word as a formatted string
    for key in alphabeticalKeys:
        file.write(f"{key} {freqDict[key][0]} {round(freqDict[key][1], 3)}\n")

    

def setFrequencyRatio(freqDict, wordCount):
    """ Specific function for calculating word occurrence ratio when given a dictionary containing string representations of words as keys and a two element list containing its 
    occurrences and a 0. The 0 is overwritten with the occurence ratio.

    Arguments:
        freqDict (dict): Dictionary containing a file's words as keys and a list of respective word occurrences and a 0 int as the values
        wordCount (int): Total word count of the file to analyze

    Returns:
        none
    """
    for word in freqDict:
        wordFreq = freqDict[word][0]

        freqDict[word][1] = wordFreq / wordCount

    return freqDict
    

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to 
    # this exercise, so you should call your code from here.
    contentList = getFileContents()
    freqDict = getWordFrequency(contentList)

    writeFreq(freqDict)
