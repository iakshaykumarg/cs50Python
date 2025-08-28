# while loop
# i = 0
# while i < 3:
#     print("meow")
#     # print(f"value of i is {i}")
#     i += 1

# for loop
# for _ in range(3):
#     print("meow")

# pythonic way to print n times
# print("meow\n" * 3,end="")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("what's n? "))
        if n>0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()