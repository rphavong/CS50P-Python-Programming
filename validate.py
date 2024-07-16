## Regular Expressions are regexes

## Validate the email address of a user
# email = input("What's your email? ").strip() # the strip() deleted spaces or in other words 'whitespace'

# if "@" in email:
#     print("Valid")
# else:
#     print("Invalid")
# ## However, the above only validates if a '@' is inputted



# ## Let's add another boolean feature, in this case '.'
# email = input("What's your email? ").strip() 

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")



# ##  However, code above is still not so good
# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")



# ## Furthermore, we could be more percise by having the code only validate if the email ends with '.edu'
# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")
# ## However, if user does not include domain such as @'gmail' it will still valid the email input



## Using 're.search'
# import re

# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if re.search("@", email):
#     print("Valid")
# else:
#     print("Invalid")
# ## This is no different to our codes above, as this only looking for a "@" that  user may input



# ## To further the 're' approach
# import re

# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if re.search(".+@.+", email): 
#     print("Valid")
# else:
#     print("Invalid")



# ## Furthermore to code above
# import re

# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if re.search(".+@.+.edu", email): # this is not so great because we could use any character where we want the dot before edu as in '.edu'
#     print("Valid")
# else:
#     print("Invalid")




# ## Improve code above
# import re

# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if re.search(r".+@.+\.edu", email): # using the 'r' is for the raw string to code to understand to print code as is!
#     print("Valid")
# else:
#     print("Invalid")
# ## However, this code is still not so good because a user can input multiple '@'s such as rob@@@ucsd.edu and code would consider as 'Valid'
# ## similarly, users could add more characters to the left and right and consider as 'Valid'


# ## Using '^' and '$' to prevent users from inputting characters before and after their actual email
# ### '^': matches the start of the string
# ### '$': matches the end of the string just before the newline at the end of the string
# import re

# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if re.search(r"^.+@.+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")
# ## However, the code above still allows for multiple "@'s" such as rob@@ucsd.edu



# ## Addressing the prevention of code validating multiple '@'s' from user by using '[]'
# ## the '[]' is used an except, specifies a set of characters
# ## [^] complementing the set
# import re

# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if re.search(r"^[^@]+@[^@]+\.edu$", email): # the [^@] is saying everything EXCEPT the '@' sign!
#     print("Valid")
# else:
#     print("Invalid")




# ## To specify a range of letters for an email validation?
# import re

# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): 
#     print("Valid")
# else:
#     print("Invalid")



## However, you can simplify the '[a-zA-Z0-9_]' from code above with simply a '\w'
## '\w' referes to word character, as well as numbers and the underscore
## note that there are others that can be found in the re library
# import re

# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if re.search(r"^\w+@\w+\.edu$", email): 
#     print("Valid")
# else:
#     print("Invalid")




# ## Furthermore, you can include multiple email domains
# import re

# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email): 
#     print("Valid")
# else:
#     print("Invalid")
# ## However, the above does not address uppercase EDU



# ## Using 're' 'flags', such as 're.IGNORECASE'
# import re

# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE): 
#     print("Valid")
# else:
#     print("Invalid")



## How to address emails that have two '.' dots after '@'
## i.e. malan@cs50.harvard.edu, this email will return as 'Invalid'
## Here we will be using the '?' as this will make the pattern optional from the code in '()' from the left of the ? mark
# import re

# email = input("What's your email? ").strip() 

# username, domain = email.split("@")


# if re.search(r"^\w+@(\w=\.)?\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE): 
#     print("Valid")
# else:
#     print("Invalid")



## Additionally, emails are popular not to have '.' before the '@'
## To address this we can simple add that in '()'
import re

email = input("What's your email? ").strip() 

username, domain = email.split("@")


if re.search(r"^(\w|\.)+@(\w=\.)?\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE): 
    print("Valid")
else:
    print("Invalid")

