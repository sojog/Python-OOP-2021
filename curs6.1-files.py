import os

file_name = 

file_handler = open("demofile3.txt", "w")
file_handler.write("Woops! I have deleted the content!")
file_handler.close()

#open and read the file after the appending:
file_handler = open("demofile3.txt", "r")
print(file_handler.read())

