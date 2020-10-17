# mindent importál
# import module.matek

from module.matek import substract, add

# nem preferált
from module.matek import *

# Ha azonos létezik, ennek nagyobb lesz a prioritása
def add(a, b):
    return 5555

print(add(2,8))
print(substract(2,8))


# https://pypi.org/
# pip install matplotlib
# pip uninstall matplotlib
# import matplotlib                               
import matplotlib.pyplot as plot
plot.plot([1,7,8,9])
plot.show()

