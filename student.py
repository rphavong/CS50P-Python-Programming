## Assigning variables 
# def main():
#     name = input("Name: ")
#     house = input("House: ")
#     print(f"{name} from {house}")

# main()



# ## Creating functions 
# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")
    
# def get_house():
#     return input("House: ")

# if __name__ == "__main__":
#     main()



# ## How to condense code above; this is an example of a 'tuple'
# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)

# if __name__ == "__main__":
#     main()



# ## What if we wanted to be more robust by preventing users from assigning a character into the wrong house?
# ## Example below will correct the user if they would have inputted 'Padma' and then 'Gryffinfor', this code will output 'Padma from Ravernclaw'
# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] == "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]

# if __name__ == "__main__":
#     main()



# ## Another approach to code above, using dictionaries
# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     student = {} ## Recall the '{}' is to create a dictionary, the code right below is adding to the dictionary
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()



# ## Alternatively to code above:
# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()



## Let's continue adding to this code to include Padma into the correct Hogwarts house
## Below is explicitly describing what each variable is, instead of using 0,1,etc.
# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()



# ## Create a data type using 'classes'
# class Student:
#     ... # This is a placeholder 


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}") # Note these differences from the code above

# def get_student():
#     student = Student()
#     student.name = input("Name: ") # Note that this is similar to dictionary, but you use attributes
#     student.house = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()



# ## Furthermore you can also approach the code above as follows
# class Student:
#     ... # This is a placeholder 


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     Student = Student(name, house)
#     return student

# if __name__ == "__main__":
#     main()



# ## Using the __init__ an instance, to initiate a method/object
# class Student:
#     def __init__(self, name, house): # note you need 'self' where it stores info into the current object, in this case Students
#         self.name = name # create a new attribute, in this came name, you can use any variable after self., but need to define variable after, such as 'name'
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)
#     return student

# if __name__ == "__main__":
#     main()



## How to approach if user were to input bogus or empty inputs?
## Using 'raise': programmer can raise an issue/error from a user
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name") # Note you can also add message into the Error output!
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()



# ## Using __str__
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"


# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()



# ## Creating your own methods
# class Student:
#     def __init__(self, name, house, patronus):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#         self.patronus = patronus

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "🦌"
#             case "Otter":
#                 return "🦦"
#             case "Jack Russel Terrier":
#                 return "🐕"
#             case _:
#                 return "🪄"

# def main():
#     student = get_student()
#     print("Expecto Patronum!")
#     print(student.charm())

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)

# if __name__ == "__main__":
#     main()



# ## Using 'properties
# ## prevents programmers from messing up attributes
# ## '@property'
# ## decorators
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     # Getter
#     @property 
#     def house(self):
#         return self._house
   
#     # Setter
#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house


# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()



# ## Also integrating error in case a user does not include a name
# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing name")
#         self._name = name
        
#     # Getter
#     @property 
#     def house(self):
#         return self._house
   
#     # Setter
#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house

# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()



## Futher cleaning the code above, integrating 'cls' from "hat.py"
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()








