szovegem = "Ez itt egy szöveg"


def legtobb_betu(szoveg):
    betuszotar = {}
    for betu in szoveg:
        if betu in betuszotar:
            betuszotar[betu] += 1
        else:
            betuszotar[betu] = 1
    return betuszotar


def leggyakoribb_3(betu_szotar):

    eredmeny = []

    betuszam = len(betu_szotar)
    """
    if betuszam > 3:
    betuszam = 3
    """

    betuszam = 3 if betuszam > 3 else len(betu_szotar)
    while len(eredmeny) < betuszam:
        maximum = 0
        betu = ''
        for kulcs, ertek in betu_szotar.items():
            if maximum < ertek:
                maximum = ertek
                betu = kulcs
        eredmeny.append(betu)
        del betu_szotar[betu]

    return eredmeny


print(leggyakoribb_3(legtobb_betu(szovegem)))
