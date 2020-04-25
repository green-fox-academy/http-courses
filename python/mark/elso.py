nev = "Márk"
kor = 28
kedvenc_gyumolcs = "mango"

# Sziasztok, Béla vagyok 40 éves!
# A kedvenc gyümölcsöm a dinnye.

# "a" + "b" -> "ab"

print("Sziasztok, " + nev + " vagyok " + str(kor) + " éves!")
print("A kedvenc gyümölcsöm a " + kedvenc_gyumolcs + ".")

print(f"Sziasztok, {nev} vagyok {kor} éves!")
print(f"A kedvenc gyümölcsöm a {kedvenc_gyumolcs}.")


print(
    f"Sziasztok, {nev} vagyok {kor} éves!\nA kedvenc gyümölcsöm a {kedvenc_gyumolcs}.")

print(
    "Sziasztok, %s vagyok %d éves!\nA kedvenc gyümölcsöm a %s." % (nev, kor, kedvenc_gyumolcs))

szoveg = "Sziasztok, {} vagyok, {} éves!\nA kedvenc gyümölcsöm a {}."
print(szoveg.format(nev, kor, kedvenc_gyumolcs))
