import sys
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("too few argument")

# if len(sys.argv) < 2:
#     sys.exit("too few argument")
# elif len(sys.argv) > 2:
#     sys.exit("too many argument")

# print(f"hello, my name is {sys.argv[1]}")


if len(sys.argv) < 2:
    sys.exit("too few argument")

for arg in sys.argv[1:]:
    print(f"my name is {arg}")