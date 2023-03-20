import os

file_name = "curs6.1.3-files-read-from-file.txt"

file_handler = open(file_name, "r")
# print(file_handler.read())

print(file_handler.readline())
print(file_handler.readline())
print(file_handler.readline())

# for x in file_handler:
#   print(x)

