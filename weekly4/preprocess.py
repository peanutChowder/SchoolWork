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

def punctuationCorrection(word):
    pass

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
    print(words)