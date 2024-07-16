## How to information from the user.
# ## Example from a twitter url how to extract the username only
# url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "") # Using the '.replace()' you can replace one arguemnt to intended. In this example we are replacing the url with nothing!
# print(f"Username: {username}")



# ## However, the code above is only considering "https://twitter.com/"
# ## Using 'removeprefix()'
# url = input("URL: ").strip()

# username = url.removeprefix("https://twitter.com/", "") # 
# print(f"Username: {username}")



# ## Using 're.sub()' to 'remove' the url to only obtain the username 
# import re

# url = input("URL: ").strip()
# username = re.sub(r"https://twitter.com/", "", url)
# print(f"Username: {username}")



# ## How to also remove other url's such as http, www, etc
# import re

# url = input("URL: ").strip()
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) 
# print(f"Username: {username}")



# ## Addressing other potential issues 
# import re

# url = input("URL: ").strip()
# if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(f"Username:", matches.group(1))



## Adding more potential issues that might be inputted by user to be more tolerant
import re

url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
