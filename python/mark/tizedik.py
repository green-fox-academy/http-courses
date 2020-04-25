# uj_generacio(matrix) -> matrix

jelenlegi_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def uj_generacio(matrix):
    uj_matrix = matrix.copy()
    for sor in range(1, len(matrix)-1):
        for oszlop in range(1, len(matrix[0])-1):
            szomszed_szam = szomszedok_osszege(sor, oszlop, matrix)
            eletben_van = matrix[sor][oszlop] == 1
            if (szomszed_szam == 2 or szomszed_szam == 3) and eletben_van:
                uj_matrix[sor][oszlop] = 1
            elif (szomszed_szam < 2 or szomszed_szam > 3) and eletben_van:
                uj_matrix[sor][oszlop] = 0
            elif not eletben_van and szomszed_szam == 3:
                uj_matrix[sor][oszlop] = 1
    return matrix


def szomszedok_osszege(sor_index, oszlop_index, matrix):
    osszeg = 0
    for sor in range(sor_index - 1, sor_index + 2):
        for oszlop in range(oszlop_index - 1, oszlop_index + 2):
            osszeg += matrix[sor][oszlop]
    return osszeg - matrix[sor][oszlop]


[print(sor) for sor in uj_generacio(jelenlegi_matrix)]
