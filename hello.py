# # Defining variables
# def hello(to):
#     print("hello,", to)

# # Ask user for their name
# name = input("What's your name? ")

# hello(name)


# # Can assign defaults
# def hello(to="world"):
#     print("hello,", to)

# hello()
# # Ask user for their name
# name = input("What's your name? ")

# hello(name)


# How to properly code so that you do not need to keep adding more code above, instead of below
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

