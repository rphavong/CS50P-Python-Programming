## Reading CSV files

# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")



# ## Similarly, to code above
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")




# ## Sorting the list of names and house in csv file
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)



## However, a better design to code above
# ## Integrating dictionaries
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)


# for student in students:
#     print(f"{student['name']} is in {student['house']}")



# ## Similarly and better to code above:
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)


# for student in students:
#     print(f"{student['name']} is in {student['house']}")



# ## How to integrate sort to code above?
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)


# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")




# ## To sort in reverse to code above
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)


# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")



# ## Sort by house?
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)


# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_house, reverse=True):
#     print(f"{student['name']} is in {student['house']}")




# ## Using lambda
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)


# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")



# ## Looking into students names and homes they grew up in
# students = []

# with open("students_homes.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name, "home": home}
#         students.append(student)


# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
# # however, note that you will get the error: 'ValueError: too many values to unpack (expected 2)'



## One appraoch to address to code above using 'csv' library
# import csv

# students = []

# with open("students_homes.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({"name": row[0], "home": row[1]})


# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")



# ## Equivalently to code above, you can define rows:
# import csv

# students = []

# with open("students_homes.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})


# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
# # Note that the code above only worked when I added " " to Harry's home 'Harry,"Number Four, Privet Drive"'



## Using Dictionary Reader
## We added the first line to "students_homes.csv" "name,home"
## The code below addressed in case the data from "students_homes.csv" was reversed, where home were to listed first and then name!
# import csv

# students = []

# with open("students_homes.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})


# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")



## How to write into a csv 
# import csv

# name = input("What's your name? ")
# home = input("Where's your home? ")

# with open("students_write.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])



## Using Dictionary Writer to write csv
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students_write.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})




