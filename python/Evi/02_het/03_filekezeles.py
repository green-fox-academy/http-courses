# File kezelés

# open()
# abszolut eleresi ut:
import os
print(os.path.dirname(os.path.abspath(__file__)))

file = open('root.txt', 'r')
print(file.read())
file.close()

with open('root.txt', 'r') as file:
    print(file.read())

print("vege")

# read, write és append mód

# read() --> egyben olvassa be
# line = file.readlines() --> listat ad vissza, egy sor lesz egy listaelem

line = file.readline() - -> soronkent

while line:
    print(line.strip())
    line = file.readline()

# file.readline()
# file.close()
# file.read()
# file.write()

# write felulirja a file megnyitasa elotti tartalmat
file.write("\nhello2")
file.close()

# UTF-8
# karakterkodolas, most a p3-ban ez a default
