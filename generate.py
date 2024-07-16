## Importing library
# import random

# coin = random.choice(["heads", "tails"])
# print(coin)



# ## Alternatively, using 'choice'
# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)


# ## Using random.randint(a, b)
# ## This will randomly choose numbers defined
# import random 

# number = random.randint(1, 10)
# print(number)


## Using 'random.shuffle(x)'
import random

cards = ["jack", "king", "queen"]
random.shuffle(cards)

for card in cards:
    print(card)
