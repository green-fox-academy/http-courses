# operatorok
# osszehasonlitas: ==,  !=, is, is not

# primitiv tipus masolasa
first_name = "Anita"
last_name = "Anita"

# osszahasonlitas
print(first_name == last_name)
print(first_name is last_name)

# referencia tipus
felhasznalo1 = {
    "first": "Adam",
    "last": "Kovacs"
}

felhasznalo2 = {
    "first": "Adam",
    "last": "Kovacs"
}

# referencia tipus osszehasonlitas
print(felhasznalo2 == felhasznalo1)
print(felhasznalo2 is felhasznalo1)

# mas nyelvekben && ||, itt and, or

# /
#   maradekos eredmenyt kapok, tehat a 2/5 --> tortszam lesz
# //
#   maradek nelkuli eredmenyt kapok
#   10 // 4 --> 2
# %
#   modulo operator, az osztas utani maradekot mutatja
#   10 % 5 --> 0
#   10 % 4 --> 2


# [:]           szeletet kivagni
# lista[1:]     elso indextol vegig
# lista[:4]     elolrol, 0. indextol 4. indexig
# lista[1:4]    1-4 indexig, 1 bennevan, 4 mar nincs benne
# lista[1:20:3] 1. indextol 20.ig harmasaval
