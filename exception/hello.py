def main():
# call a functions
    num = get_number()
    sqr = square(num)
    print(f"the square of your number is {sqr}")

#create a functions
def get_number():
    while True:
        try:
            x = int(input("which number you want to square? "))
        except ValueError:
            pass
        else:
            return x

def square(number):
    return number * number
    


if __name__ == "__main__":
    main()