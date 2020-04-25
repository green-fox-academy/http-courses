# fizzbuzz vagy piffpuff

# szam -> szoveg

oszto_szoveg_parosok = {
    3: "Piff",
    7: "Puff",
    11: "Paff"
}


def oszto_szoveg_generator(szam, parosok):
    jelen_szam_szoveges_valtozata = ""
    for (oszto, szoveg_ha_oszto) in parosok.items():
        if szam % oszto == 0:
            jelen_szam_szoveges_valtozata += szoveg_ha_oszto
    if jelen_szam_szoveges_valtozata == "":
        return szam
    return jelen_szam_szoveges_valtozata


for index in range(1, 101):
    print(oszto_szoveg_generator(index, oszto_szoveg_parosok))

# for index in range(1, 101):
#     if index % 3 == 0 and index % 7 == 0:
#         print("Piff" + "Puff")
#     elif index % 3 == 0:
#         print("Piff")
#     elif index % 7 == 0:
#         print("Puff")
#     else:
#         print(index)

# szam = 1
# egyikse = True

# while szam < 101:
#     if szam % 3 == 0:
#         print("Piff", end="")
#         egyikse = False
#     if szam % 7 == 0:
#         print("Puff")
#         egyikse = False
#     elif not egyikse:
#         print()
#     if egyikse:
#         print(szam)

#     szam += 1
#     egyikse = True
