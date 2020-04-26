from sharpie import Sharpie
from sharpie_set import SharpieSet

s1 = Sharpie('zold', 3)
s2 = Sharpie('kek', 0.5)
s3 = Sharpie('barack', 2)

sharpie_set = SharpieSet()

sharpie_set.add(s1)
sharpie_set.add(s2)
sharpie_set.add(s3)

s3.ink_level = 0

print(sharpie_set.count_usable())
sharpie_set.remove_trash()

print(sharpie_set.sharpies)