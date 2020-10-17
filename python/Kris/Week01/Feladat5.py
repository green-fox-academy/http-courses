"""def összegek(lista):
    summa = 0
    for number in lista:
        summa += number
    summa /= len(lista)
    return summa

my_list = [1, 2, 3, 4, 5]

print(int(összegek(my_list)))
"""

import statistics
lst = [1, 2, 3, 4, 5]
print(statistics.mean(lst))
