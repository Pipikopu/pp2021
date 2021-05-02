import os

while True:
    i = input("Enter command: ")
    if i == "exit":
        break
    os.system(i)

print("Finish!")