# ## Print meow 3x
# print("meow")
# print("meow")
# print("meow")

# ## How could you print 'meow' three times
# ## 'while' statement to express a loop
# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1   # This allows for the loop to stop after printing 'meow' 3 times


# ## Similarly you could do
# i = 0
# while i < 3:
#     print("meow")
#     i = i + 1


# ## Exact same code above but using '+='
# i = 0
# while i < 3:
#     print("meow")
#     i += 1


# ## 'for' loops
# for i in [0, 1, 2]: # Understand that here you're saying for a variabel 'i' in the list '0-2', it will print meow for each number in the list
#     print("meow")


# ## Similarly and better code from above, using 'range'
# for i in  range(3): 
#     print("meow")


# ## You can also use ' _ ' instead of specific variable 
# for _ in  range(3): 
#     print("meow")


# ## What about using '*' to print 'meow' 3 times?
# print("meow\n" * 3, end="")


# ## Asking the user to input a number of times to 'meow'?
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


# ## Another approach; however, this is hard coding to print 'meow' 3 times
# def main():
#     meow(3)

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()


## Editng the code above to not hard code to print 'meow' 3 times
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
