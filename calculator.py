## Creating a calculator that could then be used, in this case in relation to 'test_calculator.py'

def main():
    x = int(input("What's x? ")) # We also tested by removing 'int()'
    print("x squared is", square(x))


def square(n):
    return n * n # we tested potential bug by changing 'n * n' to 'n + n'


if __name__ == "__main__":
    main()

