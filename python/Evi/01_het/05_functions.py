# Fuggvenyek

# letrehozas
def fuggvenynev():
    pass

# parameterek
# alapertelmezett ertek megadasa
def add(n, n2 = 1):
    return n+n2

print(add(3))     # --> 4, nem adtam meg ket szamot, igy az alapertelmesett 1-et hasznalja
print(add(3, 8))  # --> 11


# return
# visszater regy ertekkel, nem fut tovabb

# ha boolean-ra van szuksegunk

# nem szep megoldas
def nagykoru(kor):
    if kor > 18:
        return True
    else:
        return False

# logikai erteket nem szep visszaadni igy leirva, hogy return True
# mivel a feltetel mar alapbol true vagy False

# szep megoldas:
def nagykoru(kor):
    return kor >= 18


# if hasznalat pythonos verzio
def ihat_pezsgot(kor):
    return "igen, ihat" if kor >= 18 else "nem ihat"


# scope: “hatotavolsag”
kor = 10


def hany_eves():
    #  letrehoz egy uj valtozot, nem a kintit irja felul
    kor = 20
    print(kor)

hany_eves()

# ha minden elemre szeretnenk megnezni egy feltetelt
# minden elem tipusa szam-e, mindegyik paros szam-e, stbstb:

lista = [1, 2, 3, 5]
vegyes = [1, 2, 3, 5, "hello"]

# nem szep verzio:
def szamlista(lista):
    szamok = True
    for szam in lista:
        if(type(szam) is not int):
            return False
    return szamok

# elegansabb pythonos megoldas
def szamlista(lista):
    return any(type(szam) == int for szam in lista)


print(szamlista(lista))
print(szamlista(vegyes))


# input() lehet bekerni inputot a felhasznalotol
nev = input()
print("szia", nev)
