## Class Methods
## '@classmethod', another type of decorator
## Example of the sorting hat to determine house of student
# ## Using 'random' that will randomly sort 'Harry' to a hogwarts house
# import random

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherine"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))


# hat = Hat()
# hat.sort("Harry")



## Using '@classmethod'
## Making class variables
import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherine"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")






