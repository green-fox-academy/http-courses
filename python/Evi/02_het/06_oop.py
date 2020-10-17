# Osztályok és Objektumok

# class

class Dog:
    nev = None
    kor = 0
    __etvagy = 0

    def __init__(self, fajta, szin):
        self.fajta = fajta
        self.szin = szin

    def eat(self):
        self.etvagy -= 1

    def play(self):
        self.etvagy += 1


morzsi = Dog('tacsi', 'barna')
print(morzsi._etvagy)

# privat valtozok nincsenek, minden elerheto igy:
# print(dir(morzsi))

# __ : jelzes hogy privatkent szeretnenk kezelni
# _ : jelzes hogy protectedkent (vedett) szeretnenk kezelni
# alapvetoen publikus minden tagvaltozo

# példányosítás
furkesz = Dog('husky', 'feher')

# tagváltozók
morzsi.nev = 'Morzsi'
morzsi.kor += 1

print(morzsi.nev)

morzsi.etvagy = 1
print(morzsi.etvagy)

del morzsi.etvagy

# metódusok
morzsi.eat()

# self
# __init__
# konstruktro fuggveny, beepitett
# a kapott parametereket allitja be a letrehozott objektumon

# "access modifier"
# private, protected, public
# Privat valtozok: https://harp.pythonanywhere.com/python_doc/tutorial/classes.html#privat-valtozok
