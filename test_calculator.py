## import from calculator you created 'calculator.py'

# from calculator import square

# def main():
#     test_square()

# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")


# if __name__ == "__main__":
#     main() 


# ## Using 'assert' to condense code above
# from calculator import square

# def main():
#     test_square()

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9


# if __name__ == "__main__":
#     main() 


# ## Using 'try' and 'except' to address AssertionError
# from calculator import square

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 sqaured was not 9")


# if __name__ == "__main__":
#     main() 



# ## Including other parameters
# from calculator import square

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 sqaured was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 sqaured was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 sqaured was not 0")


# if __name__ == "__main__":
#     main() 



## Integrating 'pytest': this will hint to you where the error might coming from!
## If needed, to Install pytest: 'pip install pytest'
# from calculator import square

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

# Then in the terminal you would run this code as:
## 'pytest test_calculator.py'



## Note that from the code above, only the first error will be reported
# ## One approach, you can break up your code by:
# from calculator import square

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9


# def test_negative():
#     assert square(-2) == 4
#     assert square(-3) == 9

# def test_zero():
#     assert square(0) == 0


## Integrtating potential TypeError, in case a none integer were to inputted
import pytest
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
