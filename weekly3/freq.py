#--------------------------------------------
#   Name: 
#   ID: 
#   CMPUT 274
#
#   Weekly Exercise 3: Word Frequency
#-------------------------------------------- 
# FREQ TEMPLATE: ADD YOUR INFORMATION TO ABOVE

# You must determine how to structure your solution.
# Create your functions here and call them from under
# if __name__ == "__main__"!

import sys

def demo_command_line():
    # the first argument is the program name
    print(sys.argv[0])

    # so the filename is the second argument
    filename = sys.argv[1]
    print(filename)
    return(filename)

def correctArgNum():
    if len(sys.argv) > 2:
        print("Too many arguments. Usage: python3 freq.py <input_file_name>")
        return False

    elif len(sys.argv) < 2:
        print("Too few arguments. Usage: python3 freq.py <input_file_name>")
        return False

    else:
        return True

def getFileContents():
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
    freqDict = {}
    maxCount = 0

    for word in contentList:
        if word not in freqDict:
            freqDict[word] = [1, 0]
        else:
            freqDict[word][0] += 1

        if maxCount < freqDict[word][0]:
            maxCount = freqDict[word][0]

    freqDict = setFrequencyRatio(freqDict, maxCount)


    # TODO: Leftoff here. just made the frequency ratio function
    print(freqDict)

def setFrequencyRatio(freqDict, maxCount):
    for word in freqDict:
        wordFreq = freqDict[word][0]

        freqDict[word][1] = wordFreq / maxCount

    return freqDict

    


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to 
    # this exercise, so you should call your code from here.
    contentList = getFileContents()
    getWordFrequency(contentList)
