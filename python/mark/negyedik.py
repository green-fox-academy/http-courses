sorokSzama = 10


def rajszolj_csillagokat(szamossag):
    i = 1
    while i < szamossag + 1:
        print(" "*(szamossag-i) + "*"*(2*i-1))
        i += 1


rajszolj_csillagokat(sorokSzama)
