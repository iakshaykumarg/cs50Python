def main():
    print_column(3)

# def print_column(height):
#     # for _ in range(height):
#         # print("#")
#     print("#\n" * height,end="")

def print_column(size):
    # for i in range(size):
    #     print("#" * size)

    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()
if __name__ == "__main__":
    main()