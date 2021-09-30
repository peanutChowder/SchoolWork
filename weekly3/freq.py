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

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to 
    # this exercise, so you should call your code from here.
    demo_command_line()
