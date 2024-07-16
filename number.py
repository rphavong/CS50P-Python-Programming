## Understanding Syntax Errors
## What if you forget to add a quotation to your code
# print("hello, world")

# ## Understand that this cannot take anything but integers, including negatives integers
# x = int(input("what's x? "))
# print(f"x is {x}")


## How to write code that can handle Value Errors, so that the output is a more friendly output instead of some type of error when an integer is not used by a user
### Value Errors and 'try' and 'except'

# try:
#     x = int(input("what's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")



# ## A better approach to code above, approach to 'NameError'
# try:
#     x = int(input("what's x? ")) # the name error is coming from this part because the int() is not accepting anything but integers
# except ValueError:
#     print("x is not an integer")

# print(f"x is {x}")


# ## How to approach the 'NameError' from code above when an integer is not inputed by the user
# try:
#     x = int(input("what's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")


## Let's refine this code even more
# ## Integrating loop, where the loop will continue until used inputs an integer
# while True:
#     try:
#         x = int(input("what's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")



# ## You can also include the break after 'x=', to minimize the number of lines of code
# ## This is logically correct because the loop will tyr to run the input of 'x' and then break
# ## If not it will go to the next line and continue the loop until an integer is inputted by user
# while True:
#     try:
#         x = int(input("what's x? "))
#         break
#     except ValueError:
#         print("x is not an integer")

# print(f"x is {x}")



# ## Let's refine even futher
# ## Creating a function
# def main():
#     x = get_in()
#     print(f"x is {x}")

# def get_in():
#     while True:
#         try:
#             x = int(input("what's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else: 
#             break
#     return x

# main()



# ## Tidy even more the code above
# def main():
#     x = get_in()
#     print(f"x is {x}")

# def get_in():
#     while True:
#         try:
#             return int(input("what's x? "))
#         except ValueError:
#             print("x is not an integer")

# main()



# ## Using the 'pass'; this will loop until an integer is inputted by user
# def main():
#     x = get_in()
#     print(f"x is {x}")

# def get_in():
#     while True:
#         try:
#             return int(input("what's x? "))
#         except ValueError:
#             pass

# main()



## Further the code above, by making a more reusable code
## The below will not hard code in defining x
def main():
    x = get_in("what's x? ")
    print(f"x is {x}")

def get_in(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()