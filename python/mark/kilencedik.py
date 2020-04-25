szam1 = 153
szam2 = 24
szam3 = 1634
szam4 = 6


# def armstrong_e(szam):
#     num = 0
#     n = len(str(szam))
#     for i in range(n):
#         x = int(str(szam)[i])
#         num = num + x**n
#     return("Armstrong szám" if num == szam else "Nem Armstrong-szám")

def armstrong_e(szam):
    return int(szam) == sum([int(i)**len(str(szam)) for i in str(szam)])


def armstrong_kiiras(szam):
    return("Armstrong szám" if armstrong_e(szam) else "Nem Armstrong-szám")


# assert armstrong_e(153) == True, "153 az egy armstrong szam"
# assert armstrong_e(135) == False, "135 az nem egy armstrong szam"

print("A(z)", str(szam1), armstrong_kiiras(szam1))
print("A(z)", str(szam2), armstrong_kiiras(szam2))
print("A(z)", str(szam3), armstrong_kiiras(szam3))
print("A(z)", str(szam4), armstrong_kiiras(szam4))

# bementrol adott szam -> input()

vizsgalando = input()

try:
    print("A(z)", vizsgalando, armstrong_kiiras(vizsgalando))
except:
    print("A(z)", vizsgalando, "nem ertelmezheto szam")
