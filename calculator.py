# ## INTEGERS (int)
# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y) # you need to identify x and y as integers

# print(z)


# ## Another better approach
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# print(x + y)


# ## Float: Number with a decimal point
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# print(x + y)


# ## Floats + Rounding numbers
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)

# print(z)


# ## Specify commas within triplets of digits such as 1,000 instead of default 1000.
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)

# print(f"{z:,}") # note this is a format string, so that python doesn't simply print out 'z'
# # by adding the ':,' within the format string this will add the ,


# ## Using division
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x / y, 2) # the 2 specifies where to round!

# print(z)



# ## Another approach to the above
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = x / y

# print(f"{z:.2f}") # specfy how many digits you want to print! So this will print to 2 decimals


# ## Defining and using return function
# def main():
#     x = int(input("What's x? "))
#     print("x squared is", square(x))


# ## Adding a square root
# def square(n):
#     return n * n

# main()


# ## Similar to the above you can use '**' to use as the power of
# def main():
#     x = int(input("What's x? "))
#     print("x squared is", square(x))


# ## Adding a square root
# def square(n):
#     return n ** 2 

# main()



## Additionally, you can use the function pow to also use as power of
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


## Adding a square root
def square(n):
    return pow(n, 2)

main()
