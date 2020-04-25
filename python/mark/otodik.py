# szamok = [1, 2, 3, 4, 5]
szamok = [1, 15]


def atlag(szamlista):
    # if len(szamlista) == 0:
    #     return None
    # return sum(szamlista) / len(szamlista)
    try:
        return sum(szamlista) / len(szamlista)
        # rizikos, hibakat eloidezheto kodreszlet
    except:
        # lefut, ha hiba keletkezett fent
        return None


atlag_ertek = atlag(szamok)

if atlag_ertek is not None:
    print(f"atlag: {atlag_ertek}")

if isinstance(atlag_ertek, float):
    print(f"atlag: {atlag_ertek}")


# számok = [1, 2, 3, 4, 5]
# Összeg = 0
# Darab = len(számok)
# for szám in számok:
#     Összeg = Összeg+szám
# Átlag = Összeg/Darab
# print("Átlag:", Átlag)
