import os

file_name = "curs6.1.2-write-result.txt"

file_handler = open(file_name, "w")
file_handler.write("Scriere in fisier pentru prima data")
file_handler.close()

#open and read the file after the appending:
file_handler = open(file_name, "r")
print(file_handler.read())


#Write - will overwrite any existing content
file_handler = open(file_name, "w")
file_handler.write("Scriere in fisier peste ceea ce a fost scris pana atunci")
file_handler.close()
file_handler = open(file_name, "r")
print(file_handler.read())


# #Append - will append to the end of the file
file_handler = open(file_name, "a")
file_handler.write("Scriere in continuare")
file_handler.close()
file_handler = open(file_name, "r")
print(file_handler.read())

# #read by file
# read_file = file_handler.read()
# print(type(read_file))