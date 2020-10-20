# to write to a file

f = open("prg1_text", "r")
g = open("news.txt", "w")
for data in f:
    data = data.rstrip("\n")  # dont use split bexoz it will write each word sepeartlu as a list
    g.write(str(data) + "\n")  # in write evrything is passed as string annd + "\n" for write nextline in newline

# to delete a file/.py/text using program

# import os
# os.remove("news.txt")


# to delete a emplty dictionay

# import os
# os.rmdir(file_path)


# to delete a dictionary with files

# import shutil
## shutil.rmtree(file_path)
