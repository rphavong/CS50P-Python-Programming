## Using 'generators'

# def main():
#     n = int(input("What's n? "))
#     for i in range(n):
#         print("🐑" * i)

# if __name__ == "__main__":
#     main()



# ## Another approach
# def main():
#     n = int(input("What's n? "))
#     for i in range(n):
#         print(sheep(i))

# def sheep(n):
#         return "🐑" * n

# if __name__ == "__main__":
#     main()



# ## Another approach
# def main():
#     n = int(input("What's n? "))
#     for s in sheep(n):
#         print(s)

# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock

# if __name__ == "__main__":
#     main()



## However, the code above is limited to printing depending on the memory and capacity of your system
## 'yield' returns one 'iterator' at a time
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()
