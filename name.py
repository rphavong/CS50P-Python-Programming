## command-line arguments
### ex. python hello.py ___
# import sys

# print("hello, my name is", sys.argv[1]) # Note that you are starting with 1 in sys.argv. This is because '0' would be the name of the file


# ## How to address the index error to the code above
# import sys

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")



# ## Or using a Conditional
# import sys

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])



# ## Using 'sys.exit' to tidy the code above
# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")

# print("hello, my name is", sys.argv[1])


# ## Addressing 'too many arguments'
# ## Note that this outputs an extra list that includes the file name
# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv:
#     print("hello, my name is", arg) 



## Using 'slice' to address the "issue" above
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:    # this will start at 1 instead of 0; where 0 would have inluded "hello, my name is name.py"
    print("hello, my name is", arg)
