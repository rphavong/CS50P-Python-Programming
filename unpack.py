## 'unpacking'

# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")



# ## Making a list
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(coins[0], coins[1], coins[2]), "Knuts")



## How to simply the code above
## 'unpacking'
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(*coins), "Knuts") # with lists we use one '*' after the variable, in this case coins



# ## How to also use the unpacking when you have a dictionary, instead of a list
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(**coins), "Knuts") # Note that here we use two '*' for dictionaries



## Using '*args' and '**kwargs'
## This allows to keep adding more values in list
# def f(*args, **kwargs):
#     print("Positional:", args)

# f(100, 50, 25, 5)



## Furthermore you can make dictionaries
def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25) # this will automatically make a dictionary
