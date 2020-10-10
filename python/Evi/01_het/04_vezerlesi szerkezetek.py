# Vezerlesi szerkezetek

# if else elif
# kondicio lehet ()-ben, de elhagyhato
kor = 15
if kor > 18:
    print("arusithato neki pezsgo")
else:
    print("nem arusithato szamara alkohol")

# elif + and

homerseklet = 20
esik = False

if homerseklet > 30:
    print("meleg van")
elif homerseklet < 30 and not esik:
    print("kellemes")
else:
    print("hideg van")

# --> kellemes

# ha csak ket ag van, nincs elif, python engedi egy sorba
print("nagykoru") if (kor >= 18) else print("kiskoru")


# for ciklus
# egy vegigmeheto dolgon megyunk vegig: lista, tuple, stb.
napok = ["hetfo", "kedd", "szerda"]
for nap in napok:
    print(nap)

for i, nap in enumerate(napok):
    print(i, nap)

for i in range(0, 10):
    print(i)

# leptetessel

for i in range(0, 10, 2):
    print(i)

# visszafele is tudunk haladni:
for i in range(10, 0, -2):
    print(i)

# while
# feltetel teljesulese
i = 0
while(i < 10):
    print(i)
    i += 1

# break: kilep a ciklusbol
# continue: atugorja az adott iteraciot
# pass: ures utasitas

for i in range(1, 10):
    if i == 7:
        continue//break//pass
    print(i)
