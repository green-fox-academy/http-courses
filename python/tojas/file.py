file = open('text.txt')
text = file.read()
print(text)
file.close()

file2 = open('text.txt', 'r')
line = file2.readline();
print(line)
file2.close()

file3 = open('text.txt', 'r')
lines = file3.readlines();
print(lines)
file3.close()

file4 = open('text.txt', 'r', encoding="UTF-8")
for line in file4:
    print(line)
file4.close()