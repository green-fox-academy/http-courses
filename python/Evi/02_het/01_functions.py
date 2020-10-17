# Függvények

# def

# valtozo beszurasa szovegbe + alapertelmezett ("default") ertek megadasa
def udvozles(nev="vendeg"):
    return "hello %s, remelem szep napod van" % nev


print(udvozles("Anna"))
print(udvozles())

# ha boolean-ra van szuksegunk

# nem szep megoldas


def nagykoru(kor):
    if kor > 18:
        return True
    else:
        return False

# logikai erteket nem szep visszaadni igy leirva, hogy return True
# mivel a feltetel mar alapbol True vagy False

# szep megoldas:


def nagykoru(kor):
    return kor >= 18


# if hasznalat pythonos verzio
def ihat_pezsgot(kor):
    return "igen, ihat" if kor >= 18 else "nem ihat"


scope

kor = 10


def hany_eves():
    kor = 20
    print(kor)


hany_eves()
print(kor)

# len()
print(len(["hello", "szombat"]))


# valamit megvizsgalni egy lista minden egyes elemen
numbers = [1, 2, 3, 4]
vegyes = [1, 2, "hello", 3]

# hosszabb megoldas


def is_number_list(lista):
    for elem in lista:
        if type(elem) is not int:
            return False
    return True


print(is_number_list(vegyes))

# pythonosabb megoldas


def szamlista(lista):
    return any(type(elem) == int for elem in lista)


print(szamlista(vegyes))
