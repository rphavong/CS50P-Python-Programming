import sys # Recall that this is package allows for you to use the command line arguments

from sayings import hello ## Note here you are calling the code you created from the file 'sayings.py'

if len(sys.argv) == 2:
    hello(sys.argv[1])

