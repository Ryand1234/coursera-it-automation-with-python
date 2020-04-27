import os

print(os.path.exists("hello.txt"))
os.rename("hello.txt", "Hello.txt")
print(os.path.exists("Hello.txt"))
print(os.path.exists("hello.txt"))

