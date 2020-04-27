import os

print("Size: ",os.path.getsize("Hello.txt"))

import datetime
timestamp = os.path.getmtime("Hello.txt")
print(datetime.datetime.fromtimestamp(timestamp))

print(os.path.abspath("Hello.txt"))
