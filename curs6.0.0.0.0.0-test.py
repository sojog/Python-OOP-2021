#Importarea modului os (operating system) pentru lucru cu fisiere
import os

# Get absolute path
absolute_path = os.path.abspath("./")
print(absolute_path)

# Get current working directory - 
path = os.getcwd()
print(path)


#Iterarea prin folderul curent
for root, directories, files in os.walk(path):
        for filename in files:
           print(filename)