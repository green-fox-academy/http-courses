szoveg1 = "dog goat dad duck doodle never"
szoveg2 = "apple"
szoveg3 = "racecar"
szoveg4 = ""


def palindromok(szoveg):
    kezd = 0
    hossz = len(szoveg)
    palindrom = []
    while kezd < hossz:
        vegz = kezd + 3
        while vegz < hossz+1:
            reszlet = szoveg[kezd:vegz]
            if reszlet == reszlet[::-1]:
                palindrom.append(reszlet)
            vegz += 1
        kezd += 1
    return(palindrom)


print(palindromok(szoveg1))
print(palindromok(szoveg2))
print(palindromok(szoveg3))
print(palindromok(szoveg4))

assert palindromok(szoveg2) == [], "apple szovegnel nem kellene, hogy legyen"
