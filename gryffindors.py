# ## Calling out students from gryffindor from our dictionary
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)



# ## Approaching code above using 'filter'
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]

# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])



## Using 'dictionary comprehensions
# ## Creating dictionaries "on the fly"
# students = ["Hermione", "Harry", "Ron"]

# gryffindors =[]

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# print(gryffindors)



# ## More simplified from code above
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# print(gryffindors)



# ## What if I wanted only one big dictinary? == dictionary comprehension application
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)



## Adding a numeration into our list
# ## One approach 
# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])



## 'enumerate' approach
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)

