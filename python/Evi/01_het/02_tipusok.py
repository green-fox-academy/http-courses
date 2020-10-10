# Típusok
# int: egesz szam
#   - nagy szam, alulvonasokkal tehetjuk olvashatobba: 1_000_000
#   - ha pont van benne, az onnantol mar tortszamnak szamit
# float: lebegopontos tortszam
#   - kerekites: round(3.4252342342343, 2) --> ket tizedesjegyig
# bool: logikai, boolean, True vagy False
#   - 0, None, ures string: False-ra ertekelodik ki
#   - "string", nem 0 szam True-ra
# string
#   - ha benne is akarunk macskakormot: \ karakter

print("azt mondta: \"persze\" ")

#   - osszefuzes, behelyettesites

keresztnev = "Anna"
vezeteknev = "Nagy"
print(vezeteknev + " " + keresztnev)
print("Sziasztok, %s vagyok" % keresztnev)

#   - szamot stringhez adni: at kell konvertalni a str() beepitett fugvennyel
#   - first_name[1] --> nulladik karaktert mutatja, miert azt, mert 0-s indexu
#   - hany betus:

len("Anna")

#   - megnezhetek belole tobb betut is egyszerre, egy intervallumban
# az elso 3 betu lesz benne, 0,1,2, balrol zart, jobbrol nyitott
keresztnev[0:3]

orszag = "Magyarorszag"
orszag[0:10:2]      # 0-tol 10-ig kettesevel haladjon
#   - tudok masolni is stringet
#   first_name = "Anita"
#   masolat = firs_name[::]
#   --> igy primitiv tipusokat tudok masolni

#   - mondat --> szavak

udvozles = "Szep reggelt mindenkinek"
udvozles.split(" ")

#   - ha mindent nagybeture valtoztatnank: string.upper() vagy epp string.lower()
#   - mondatban kicserelni egy szot: mindat.replace(regiszo, ujszo)
#   - szovegbe valtozot behelyettesiteni: %s %f %d  --> szoveg, szam, tortszam

# list: gyujtemeny, []
gyumolcsok = ["alma", "korte", "narancs"]

# hozzaadni: tobbfelekepp
gyumolcsok.append("dinnye")
gyumolcsok = gyumolcsok + ["eper"]
gyumolcsok += ["ananasz"]

# tartalmaz-e vaamit a lista?
"ananasz" in gyumolcsok  # --> True

# megforditani a listat:

print(gyumolcsok[::-1])

# elem torlese
gyumolcsok.remove("ananasz")

# beszurni konkret indexu helyre:

# tuple:
# - () koze tesszuk az ertekeket
# - majdnem ugyanolyan, mint a lista, de nem modosithatoak az elemei

het_napjai = ("hetfo", "kedd", "szerda", "csutortok", "pentek")
# - ha csak egy elemu, de szeretnenk ha tuple lenne, kell utana egy vesszo
szekhely = ("Budapest",)

# dictionary:
# - osszetartozo kulcs-ertek parok vannak, {}

felhasznalo = {
    "nev": "Dani",
    "kor": 20
}

felhasznalo["nev"]

# - ha nem letezo kulcsot kerunk le —> hibat kapunk
# - ha a get-et hasznaljuk mikor kulcsot kerunk le —> nem letezo kulcsnal None, nem hiba, biztonsagosabb
felhasznalo.get("cim")


# - pop —> torles, felhasznalo.pop(’name’) a name kulcsot es a hozza tartozo erteket is torli
# - dict.keys() —> kulcsok listajat adja vissza
# hozzaadni

felhasznalo["cim"] = "Budapest"
