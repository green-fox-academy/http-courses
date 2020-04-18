# Készítsünk egy function-t, ami ki tudja nyomtatni egy változó típusát
def tipust_nyomtat(variable):
    print(type(variable))


# Készítsünk egy function-t, ami visszaadja a leghosszabb szót egy mondatból
def return_longest_word(sentence):
    words = sentence.split(" ")     # Lista
    longest_word = ""

    for elem in words:
        if (len(elem) > len(longest_word)):
            longest_word = elem

    return longest_word


tipust_nyomtat(1)
print(return_longest_word("Ez egy különösen hosszú mondat"))


matrix = [[i+j*3 for i in range(3)] for j in range(3)]
#matrix = [[0] * 3] * 3
print(matrix)

n = 10
for i in range(1, 2 * n, 2):
	print(("*" * i).center(2 * n))