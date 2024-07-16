## Constants

# ## Here you are setting a variable of the times to meow, where it is not hardcoded within a 'range()'
# MEOWS = 3

# for i in range(MEOWS):
#     print("meow")



# ## Better coding the code above using 'class'
# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")

# cat = Cat()
# cat.meow()



## 'type hints'
## 'mypy' can be used to detect errors prior to running a code
## Example below, after typing this code and saving, run in the command line:
### mypy meows.py
### the above will output: "error: Argument 1 to "meow" has incompatible type "str"; expected "int"  [arg-type] Found 1 error in 1 file (checked 1 source file)"
# def meow(n: int): # note here we input 'n: int' 
#     for _ in range(n):
#         print("meow")

# number = input("Number: ")
# meow(number)



## Suggestion to error above, defining each variable to be a specific class, such as 'int, str, etc ... '
# def meow(n: int):
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# meow(number)



# ## Using mypy to detect another potential error
# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# meows: str = meow(number) #error would be due to this line of code
# print(meows) 



## Approaching error in code above
# ## Now the code below will not output "None" after meowing the number of times inputed by user
# def meow(n: int) -> str:
#     """Meow n times.""" # Note this is the best practice to document to annotate code!
#     return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="") 



# ## Similarly to annotation above, we can further annotate code as below
# def meow(n: int) -> str:
#     """Meow n times.
    
#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="") 



## How to make code command line friendly
## Note the -n in command line means to print a number of times
## In the command line you can type "python meows.py -n 3" to ask the command line to print meow 3 times
# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py")



## 'argparse' library
## This will simplify the code above
## Futhermore, we created more information in the '-h' when a user uses this in the command line that specifies what each syntax means
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int) # the 'default' allows for the user to input only 'python meows.py' without defining how many times to print such as 'python meows.py -n 3'
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
