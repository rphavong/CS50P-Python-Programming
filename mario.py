## Abstractions

# ## Printing columns
# def main():
#     print_column(3)


# def print_column(height):
#     for _ in range(height):
#         print("#\n" * height, end="")


# main()



# ## Printing in row
# def main():
#     print_row(4)


# def print_row(width):
#     print("?" * width)


# main()



# ## Another approach to above
# def main():
#     print_square(3)

# def print_square(size):
#     # For each row in square
#     for i in range(size):
#         # For each brick in row
#         for j in range(size):
#             # Print brick
#             print("#", end="")

#         print()


# main()



# ## A little more refined approach to code above
# def main():
#     print_square(3)

# def print_square(size):
#     for i in range(size):
#         print("#" * size)

# main()


## Or another approach
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()



