# ## Calling for json files from url
# import requests
# import sys

# if len(sys.argv) != 2: # this forces used to include two arguments, name of file/song and then the name of artist
#     sys.exit()  # this will exit when used does not satisfy the argument above

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) # This is addressing the url and allowing the second portion for the user to determine the artist

# print(response.json())



# ## Integrating the json library
# ## This print output a bit better for user freindly
# import json
# import requests
# import sys

# if len(sys.argv) != 2: 
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) # This is addressing the url and allowing the second portion for the user to determine the artist

# print(json.dumps(response.json(), indent = 2))



## Defining data you want to extract from the respective json file
## note that the output will extract 50 songs from the respective band inputted, in this case from the band 'weezer' after inputting in terminal 'python itunes.py weezer'
import json
import requests
import sys

if len(sys.argv) != 2: 
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]) # Note that here we changed in the url '...limit=1...' to '...limit=50...'

o = response.json()
for result in o["results"]:
    print(result["trackName"])
