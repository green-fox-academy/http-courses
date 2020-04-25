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


# jobbra forgat
a = [
    [1, 2, 3, 1],
    [4, 5, 6, 4],
    [7, 8, 9, 7],
    [10, 11, 12, 13]
]
for row in a:
    print(row)

# b = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]

b = a.copy()

print(">>>>>>")

for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][(len(a))-1-i] = a[i][j]


for row in b:
    print(row)
