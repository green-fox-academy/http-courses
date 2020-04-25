class PostIt:
    hatter_szin = ''
    szoveg = ''
    szoveg_szin = ''

    def __init__(self, hatter_szin, szoveg, szoveg_szin):
        self.hatter_szin = hatter_szin
        self.szoveg = szoveg
        self.szoveg_szin = szoveg_szin

post_it_1 = PostIt('sarga', 'Elso otlet', 'kek')
post_it_2 = PostIt('rozsaszin', 'Hurra!', 'fekete')
post_it_3 = PostIt('zold', 'Szuper!', 'barna')
