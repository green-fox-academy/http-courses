# https://docs.python.org/3/library/functions.html#open

# Mindent beolvas
file = open("text.txt", "r", encoding="UTF-8")
content = file.read()
# print(content)
file.close()

# Soronként olvas be
file2 = open("text.txt", "r", encoding="UTF-8")
content = file2.readline()
# print(content)
content = file2.readline()
# print(content)
content = file2.readline()
file2.close()

# Eredmény listába kerül
file3 = open("text.txt", "r", encoding="UTF-8")
content = file3.readlines()
# print(content)
file3.close()

file4 = open("text.txt", "r", encoding="UTF-8")
for line in file4:
    pass
    # print(line)

file4.close()

#Felülír
# file5 = open("text.txt", "w")
# file5.write("sokadik sor")
# file5.close()

#Append
import os
print(list(os.linesep))

file5 = open("text.txt", "a")
file5.write("sokadibb sor" + os.linesep)
file5.close()

with open("text.txt", "r") as file6:
    content = file6.readline()
    print(content)





