## Lists
# names = [] # empty list

# for _ in range(3):
#     names.append(input("What's your name? "))

# # Sort alphabetically using 'sorted()'
# for name in sorted(names):
#     print(f"hello, {name}")

# ## This output will let you to input three names and then sorts alphabetically


# ## Saving file from the list you used, instead of inputting names every time
# name = input("What's your name? ")

# file = open("names.txt", "w") # here you are opening a 'names.txt' file and the 'w' means to write a file
# file.write(name) # this lets you to write
# file.close() # this closes the file

## However, the code above will only save the last name you inputted, which is basically overwritiing each time
# ## To approach this 
# name = input("What's your name? ")

# file = open("names.txt", "a") # here you are appending, instead of overwriting the file 
# file.write(name) 
# file.close()

## However, the above is only writing the names on the same line such as "HermioneHarryRon"
# ## To appraoch this
# name = input("What's your name? ")

# file = open("names.txt", "a") 
# file.write(f"{name}\n") # this will allow to save names inputted to write in separate lines
# file.close()


# ## What if we did not include 'file.close()'
# ## You can use 'with'
# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# ## How to read the names of an existing file?
# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line)

### However, the code above will print extra empty lines
## How to approach issue above?
# ## Using 'line.rstrip()'
# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())


# ## You can condense code above:
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())



# ## Integrating sorting of the names in alphabetical order:
# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())


# for name in sorted(names):
#     print(f"hello, {name}")


# ## We can also appraoch above by:
# with open("names.txt") as file:
#     for line in sort(file):
#         print(f"hello,", line.rstrip())



## How to reverse the sort of alphabetically listed names
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())


for name in sorted(names, reverse=True): # by default the sort will list names alphabetically from A-Z; however, here we can see when set to 'reverse=True' it will go from Z-A
    print(f"hello, {name}")

