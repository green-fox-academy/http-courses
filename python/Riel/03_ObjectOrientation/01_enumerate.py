# Beépített függvények
# https://docs.python.org/3/library/functions.html#abs

nevek = ["Anita", "Béla", "Cecil", "Dénes", "Enikő"]

for nev in nevek:
    print(nev)

for i, nev in enumerate(nevek):
    print(i, nev)

print(type(enumerate(nevek)))

for i, nev in enumerate("kutyuli"):
    print(i, nev)

# destructuring: 

elso = nevek[0]
masodik = nevek[2]
print(elso)

elso, masodik, harmadik, negyedik, otodik = nevek
print(elso)

elso, masodik, *maradek = nevek
print(elso, masodik, maradek)
