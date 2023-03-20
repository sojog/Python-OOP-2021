#Importarea modului os (operating system) pentru lucru cu fisiere
import os

# Get absolute path
absolute_path = os.path.abspath("./")
print(absolute_path)

# Get current working directory - 
path = os.getcwd()
print(path)

#Redenumirea unui fisier
#os.rename("curs6.0-test.py","curs6.0.0.0.0.0-test.py")
# os.rename("curs6.0.0.0.0.0-test.py", "curs6.0-test.py")



#Iterarea prin folderul curent 
# for root, directories, files in os.walk(path):
#         for filename in files:
#            print(filename)

# Iterarea doar prin anumite fisiere
# for f in os.scandir("./"):
#     print(f.name)


dir_list = os.listdir(path) 
print(len(dir_list))



# ## Deschiderea/pentru scriere a unui fisier
new_file_name = 'curs6.alaska.py' 
with open(new_file_name, 'w') as fp: 
    pass

## Echivalent cu 

f = open(new_file_name, "w")
f.close()




# os.remove(new_file_name)


## Deschiderea/pentru scriere a unui fisier
if os.path.exists(new_file_name):
  os.remove(new_file_name)
else:
  print("Fisierul nu exista")




dir_list = os.listdir(path) 
print(len(dir_list))