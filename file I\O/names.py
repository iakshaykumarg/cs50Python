# names = []

# for _ in range(3):
#     names.append(input("what's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("what's your name? ")
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")
# # file.close

with open("names.txt","r") as file:
    for line in file:
        print(f"hello, {line.rstrip()}")