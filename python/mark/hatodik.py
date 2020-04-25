# egy jo megoldas

# matrixom = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# def balraforgat(matrix):
#     eredmeny = []
#     sorhossz = len(matrix[0])
#     for i in range(sorhossz)[::-1]:
#         ujsor = []
#         for sor in matrix:
#             ujsor.append(sor[i])
#         eredmeny.append(ujsor)
#     return eredmeny


# ujmatrix = balraforgat(matrixom)
# for sor in ujmatrix:
#     print(sor)


# egy masik jo megoldas

# jobbra forgat
# a = [
#     [1, 2, 3, 1],
#     [4, 5, 6, 4],
#     [7, 8, 9, 7],
#     [10, 11, 12, 13]
# ]
# for row in a:
#     print(row)

# b = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]

# b = a.copy()

# print(">>>>>>")

# for i in range(len(a)):
#     for j in range(len(a[0])):
#         b[j][(len(a))-1-i] = a[i][j]


# for row in b:
#     print(row)

# harmadik jo megoldas

matrix = [
    [1, 2, 3, 1],
    [4, 5, 6, 4],
    [7, 8, 9, 7],
    [10, 11, 12, 13]
]

# print(matrix)

for elem in list([list(sor) for sor in zip(*matrix)][:: -1]):
    print(elem)

# list(list(x) for x in zip(*matrix))[:: -1])
# list comprehension

# [muvelet(valtozo_elnevezes) for valtozo_elnevezes in miben]

# megegyezik azzal, hogy:

# for valtozo_elnevezes in miben:
#      muvelet(valtozo_elnevezes)
