from sharpie import Sharpie
from sharpie_set import SharpieSet

sharpie_set = SharpieSet()

zold_sharpie = Sharpie('zöld', 1)
kek_sharpie = Sharpie('kék', 2)
piros_sharpie = Sharpie('piros', 4)
rozsaszin_sharpie = Sharpie('rózsaszín', 5)

sharpie_set.add(zold_sharpie)
sharpie_set.add(kek_sharpie)
sharpie_set.add(piros_sharpie)
sharpie_set.add(rozsaszin_sharpie)

#print(sharpie_set.count_usable())

zold_sharpie.use()
kek_sharpie.use()
piros_sharpie.use()
rozsaszin_sharpie.use()

# print(zold_sharpie.tinta_mennyiseg)
# print(kek_sharpie.tinta_mennyiseg)
# print(piros_sharpie.tinta_mennyiseg)
# print(rozsaszin_sharpie.tinta_mennyiseg)

kek_sharpie.tinta_mennyiseg = 1
piros_sharpie.tinta_mennyiseg = 1

kek_sharpie.use()
piros_sharpie.use()
print(kek_sharpie.tinta_mennyiseg)
print(piros_sharpie.tinta_mennyiseg)
print(sharpie_set.count_usable())
sharpie_set.remove_trash()
sharpie_set.printList()