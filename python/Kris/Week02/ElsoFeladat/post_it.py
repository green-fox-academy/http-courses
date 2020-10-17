# https://docs.python.org/3/library/functions.html
# sor.stip() leveszi a sortörés karaktereket, és azokat nem olvassa be
# with open magától lezárja a filet, file = open() nem, ott kell file.close()
# file.readlines() listába rakja a sorokat
# file.read() az egész file-t beolvassa (stringként, nem lesz benne \n karakter)
#import math vagy from math import sin, cos
#import fileName és utána fileName. => változók, függvények
#pip - python csomag telepítő
#pip install csomagnév
# import csomag (vagy csomag.valami) as
#pip install csomagnév --upgrade, pip uninstall csomagnév

class PostIt:
    def __init__(self, hatter_szin, szoveg, szoveg_szin):
        self.hatter_szin = hatter_szin
        self.szoveg = szoveg
        self.szoveg_szin = szoveg_szin

sarga_postit = PostIt('sárga', 'Első ötlet!', 'kék')
rozsaszín_postit = PostIt('rózsaszín', 'Hurrá!', 'fekete')
rozsaszín_postit = PostIt('zöld', 'Szuper!', 'barna')
print(sarga_postit.hatter_szin)
