## Testing 'hello.py'
# from hello import hello

# def test_hello():
#     hello("Robby") == "hello, Robby"

## Note the code above will not work because it would not return a value (hint: no 'return' value), also in 'hello.py' originally
## How to approach code above
# from hello import hello

# def test_hello():
#     hello("Robby") == "hello, Robby"


# ## Adding 'assert'
# from hello import hello

# def test_hello():
#     assert hello("Robby") == "hello, Robby"
#     assert hello() == "hello, world"



# ## Let's test code above to have multiple tests to obtain a clearer understanding of a potential error/bug
# from hello import hello

# def test_default():
#     assert hello() == "hello, world"

# def test_argument():
#     assert hello("Robby") == "hello, Robby"



## Testing for a list of names
from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"



## Create new