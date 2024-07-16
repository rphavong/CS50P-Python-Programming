## Using the modular '%' where if the integer has a remainder of a specified number, in this case 2
## Implementig if a number is even or odd
## Or can a number be divided by 2 without remainders, which will determine if a number is even
# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# ## Another approach, using boolean, 'bool' (True or False)
# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else: 
#         return False
    
# main()


# ## Pythonic syntax, where the code above can be simplified more
# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     return True if n % 2 == 0 else False
    
# main()


## Even more simplified from the above:
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0 # Note that this is your boolean expression
    
main()
