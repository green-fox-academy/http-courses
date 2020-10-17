# Beépített függvények

# abs()
print(abs(-3))

# enumerate()
napok = ["hetfo", "kedd", "szerda", "csutortok", "pentek"]
for nap in napok:
    print(nap)

for i, nap in enumerate(napok):
    print(i + 1, nap)

# nem enumerate, de dictionary tipuson vegigmenni ciklussal igy lehet:
hallgato = {
    "nev": "Anita",
    "kor": 16,
    "lakhely": "Szeged"
}

for key, value in hallgato.items():
    print(key, value)


# isinstance()
print(type("hello"))
print(isinstance("kutya", str))

# max()
print(max([2, 4, 5, 6]))
print(max('applEz'))

# min()
print(min([2, 4, 5, 6]))

# reversed()
# for string
seq_string = 'Python'
print(list(reversed(seq_string)))


# round()
print(round(3.143248739473928, 4))

# sum()
print(sum((1, 2, 3, 4)))

# list.index()
napok = ["hetfo", "kedd", "szerda", "csutortok", "pentek"]

# print(napok.index("vasarnap"))
# not in list --> hibakezeles!

# Konverziók

szam = input()
print(type(szam))
# inputbol kapott ertek mintig string tipusu lesz, akkor is ha szamot irok be!

szam = int(szam)
print(type(szam))

# float()
print(type(float("3.24")))

# list()
print(list('apple'))

# str()
print(str(123))
