str1, str2 = "Ungváli", "Péter"

# Fűzzük egybe a két string-et egy szóközzel együtt
name = str1 + " " + str2

# Adjuk hozzá, hogy "ma sajnos nincs jelen"
name += " ma sajnos nincs jelen"

# Nyerjük ki az első és utolsó elemét
first_letter = name[0]
first_letter = name[-1]
first_letter = name[len(name)-1]

# Módosítsuk az üzenetet (Ungvári a helyes)
modified = name.replace("l","r")

# Nyomtassunk ki minden szót egymás alá:
szavak = name.split(" ")

for szo in szavak:
    print(szo)
else:                   # Akkor fut le ha a for sikeresen végigment
    print("random")


# Készítsünk egy listát
lista = [1,2,3]

# Hányadik elem a "sajnos"
index = szavak.index("sajnos")
print(szavak)
print(index)

# Vegyük ki az első két elemet egy új listába
uj_lista = szavak[:2]
print(uj_lista)

# Szúrjuk be a 11-es elemet
my_list = [1,2,3,4,5,6,7,8,9,10]
my_list.insert(len(my_list), 11)

# Módosítsuk a második elemet -2
my_list[1] = -2


# Töröljük az -2 elemet
my_list.remove(-2)
print(my_list)

# Ellenőrizzük, hogy a "-2" elem nincs már benne a listában
if (-2 not in my_list):
    print("Nincs benne a -2")

# vegyük ki a 4. elemtől kezdődően minden másodikat
my_list = [1,2,3,4,5,6,7,8,9,10]
uj_list = my_list[3::3]
print(uj_list)

# Írjunk egy loop-ot, ami addig kér új számot, ameddig az > nem lesz mint 10
number = 0
while number < 10:
    number = int(input())

print(type(szavak))