with open("hello.txt") as file:
    for line in file:
        print(line)

with open("hello.txt") as file:
    for line in file:
        print(line.strip())
