## How to clean up user's inputs
# name = input("What's your name? ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")



# ## However, the code still needs work becuase it does not consider other potential issues
# import re
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last, first = matches.groups()
#     name = f"{first} {last}"
# print(f"hello, {name}")



# ## Similarly you can approach the above code by:
# import re
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last = matches.group(1)
#     first = matches.group(2)
# print(f"hello, {name}")




# ## Similarly to code above, we can concantinate 
# import re
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")




# ## Furthermore we can add a '?' to tolerate commas and no spacing from user
# ## i.e. if a user were to input "Malan,David"
# import re
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), ?(.+)$", name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")



# ## However, code above does not consider further spaces from a user
# ## i.e. if a user were to type "Malan,       David"
# ## we can simple approach this by changing the '?' from above to "*"
# import re
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")




## How to combine operations/code above
## Using ':=' walrus operator
import re
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
