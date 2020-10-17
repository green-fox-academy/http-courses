üdvözlés = "Sziasztok" 
vezetéknév = "Kovács"
keresztnév = "Krisztián"

másolat = keresztnév[:]

üdvözlés = üdvözlés + " "
# üdvözlés += " "

hosszú_üdvözlés = üdvözlés + vezetéknév + " " + keresztnév + " vagyok"

valtozo = hosszú_üdvözlés.split(" ") # listát készít minden egyes szóból, amit a szóközöknél választ el

gyümölcs = "alma"

# új értéket tudunk adni a már létező változónak
gyümölcs = "körte"

nev = "Nagy Sándor"

kor = 33

# print("Sziasztok, " + nev + " vagyok, " + str(kor) + " éves!\nA kedvenc gyümölcsöm a " + gyümölcs + ".")
# print(f"Sziasztok, {nev} vagyok, {kor} éves!\n A kedvenc gyümölcsöm a {gyümölcs}.")
print("Sziasztok, %s vagyok, %d éves!\n A kedvenc gyümölcsöm a %s" % (nev, kor, gyümölcs))

lista = [1, 2, 3, "cica", 3.14, 1, 1, 1]

#lista.append(42)

# lista = lista + ["banán"]
lista += ["banán"]

lista.insert(3, 'Python')

állat = "cica"

#lista_másolat = lista
lista_másolat = lista[:]
# lista_másolat += [14]

lista += [14]

igaz = lista == lista_másolat

# print(lista)

lista[0] = 27 # a lista 0. indexén lévő elem értékének megváltoztatása

lista.remove("cica") # elem törlése

my_tuple1 = (1, "cica", 3.14)

my_tuple2 = (42,) # my_tuple2 = (42) esetén a változónk csak egy szám lesz, kell a vessző, hogy tuple legyen

result_tuple = my_tuple1 + my_tuple2

# print(result_tuple.index("cica"))

szótár = {1: "alma", 2: "körte", "kutya": 2, 3: [1, 2, 3], None: 2}

szótár["gyümölcs"] = "banán"

#print(szótár)

a = 2
b = 4
c = 5

# (a = a + 1) == (a += 1)

a *= b


if (a != b):
    print("ők egyenlőek")
elif a > b:
    print("a nagyobb, mint b")
elif a < b:
    print("b nagyobb, mint a")
else:
    pass
#    print(" ")

napok = ["hetfo", "kedd", "szerda"]

for nap in range(2, 9, 2):
    pass
    # print(nap)

while (a < c):
    print(a)
    a += 1
    break

print(a)
