def main():
    x = get_int()
    print(f"x is {x}")


#try block
def get_int():
    while True:
        try:
            x = int(input("what's x? "))
        # exception handling
        except ValueError:
            # print("x is not an integer")
            pass
        else:
            return x

main()