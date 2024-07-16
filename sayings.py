## Creating a library to be used for 'say_ContinutationToSayings.py'
# def main():
#     hello("world")
#     goodbye("world")

# def hello(name):
#     print(f"hello, {name}")


# def goodbye(name):
#     print(f"goodbye, {name}")

# main()

## You need to also include this portion, instead of simply 'main()'
## Reason being that when you use this as code above, the main() will automatically output: 
### hello, world
### goodbye, world
### hello, Robby

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__": # using the '__name__'  
    main()

