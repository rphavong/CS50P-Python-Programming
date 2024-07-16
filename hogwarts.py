## Lists
# students = ["Hermione", "Harry", "Ron"]

# print(students[0]) # note we are using 0
# print(students[1])
# print(students[2])


# ## Better code for above where we could also take into consideration more students added to the list
# students = ["Hermione", "Harry", "Ron"]

# for student in students:    # note that 'student' without the "'s" is a random variable we are using 
#     print(student)



# ## Prefer using a variable?
# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(students[i])



# ## What if you wanted to 'rank' your students, based on the order of the list
# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i]) # the 'i + 1' allows for the list to rank starting at 1 in the list, instead of default of 0



## Dictionaries 'dict', allows to associate keys and values
# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


# ## This is creating a dictionary, where it is essentially the save as the code above
# students = {"Hermione"  : "Gryffindor", 
#             "Harry"  : "Gryffindor", 
#             "Ron"  : "Gryffindor", 
#             "Draco"  : "Slytherin"
# }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])



# ## Even better to code above
# students = {"Hermione"  : "Gryffindor", 
#             "Harry"  : "Gryffindor", 
#             "Ron"  : "Gryffindor", 
#             "Draco"  : "Slytherin"
# }

# for student in students:
#     print(student)


# ## To also print the key and value
# students = {"Hermione"  : "Gryffindor", 
#             "Harry"  : "Gryffindor", 
#             "Ron"  : "Gryffindor", 
#             "Draco"  : "Slytherin"
# }

# for student in students:
#     print(student, students[student], sep= ", ")



## Integrating more data (variables) into our list
students = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus": "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus": "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
