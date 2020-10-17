"""
Készíts egy PostIt osztályt, amelynek van 3 tagváltozója:

hatterSzin
szoveg ami rajta van
szovegSzin Készíts pár példa objektumot:
sárga posztit kék szöveggel: "Első ötlet"
rózsaszínű posztit fekete szöveggel: "Hurrá!"
zöld posztit barna szöveggel: "Szuper!
"""

class PostIt:
    def __init__(self, hatterSzin, szoveg, szovegSzin):
        self.hatterSzin = hatterSzin
        self.szoveg = szoveg
        self.szovegSzin = szovegSzin

sargaPostIt = PostIt("sárga", "Első ötlet", "kék")
pinkPostIt = PostIt("pink", "Hurrá", "fekete")
zoldPostIt = PostIt("zöld", "Szuper!", "barna")
