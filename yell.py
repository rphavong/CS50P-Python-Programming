# def main():
#     yell("This is CS50")

# def yell(phrase):
#     print(phrase.upper())

# if __name__ == "__main__":
#     main()



# ## Integrating a list and unpacking
# def main():
#     yell(["This", "is", "CS50"])

# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

# if __name__ == "__main__":
#     main()



# ## More user friendly, adopting *args
# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

# if __name__ == "__main__":
#     main()



# ## Using 'map' which applies a function to each argument
# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = map(str.upper, words)
#     print(*uppercased)

# if __name__ == "__main__":
#     main()



## Using 'list comprehensions'
## This allows to create a list "on the fly"
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()
