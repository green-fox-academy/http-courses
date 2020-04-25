name = "Ungvári Péter ma sajnos nincs jelen"
sentence = name.split(" ")

# Nyomtassunk ki minden szót egymás alá:
for word in sentence:
    print(word)

# my_list = [1, 2, 3, 4, 5]
# Hányadik elem a "sajnos"
index = sentence.index("sajnos")

# Vegyük ki az első két elemet egy új listába
part_list = sentence[0:2]           # Slicing
part_list = sentence[:2]            # Implicit: az első elemtől kezdve


# Vegyük ki az összes elemet a másodiktól kezdve
part_list = sentence[1:]            # Implicit: az utolsó elemig


# vegyük ki a 4. elem után következő sorból minden másodikat
my_list = [1,2,3,4,5,6,7,8,9,10]
my_list = my_list[4::2]             # 3. paraméter: lépésköz


# Szúrjuk be a "újra" kifejezést a "sajnos" szó után
name = "Ungvári Péter ma sajnos nincs jelen"
sentence = name.split(" ")
index = sentence.index("sajnos")
sentence.insert(index,"újra")


# Módosítsuk a második elemet Endrére
sentence[1] = "Endre"

# Adjunk hozzá egy új elemet: "köztünk"
sentence.append("köztünk")

# Ellenőrizzük, hogy a "köztünk" elem nincs már benne a listában
if ("köztünk" not in sentence):
    print("Nincs már benne")
else:
    print("Benne van")

# Ciklusok
# Számoljunk el 1-től 50-ig
for i in range(1, 51, 2):
    print(i)

# Írjunk egy loop-ot, ami addig kér új számot, ameddig az > nem lesz mint 10
number = 0
while (number < 10):
    print("Kérlek adj egy számot:")
    number = int(input())

# print(index)
# print(sentence)