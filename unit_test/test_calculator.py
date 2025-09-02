from calculator import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    # try:
    #     assert square(2) == 4
    # except AssertionError:
    #     print("square of 2 was not 4")
    # try:
    #     assert square(3) == 9
    # except AssertionError:
    #     print("square of 3 was not 9")
    # try:
    #     assert square(-2) == 4
    # except:
    #     print("sqaure of -2 was not 4")
    # try:
    #     assert square(-3) == 9
    # except:
    #     print("sqaure of -3 was not 9")
    # try:
    #     assert square(0) == 0
    # except:
    #     print("sqaure of -3 was not 9")

if __name__ == "__main__":
    main()