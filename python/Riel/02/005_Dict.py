# Készítsünk egy dictionary-t számozott szövegekkel

my_list=[1,2,4,5,7]                 # Lista
my_tuple=(1,2,4,5,7)                # Tuple
my_dict = {1:"Hétfő", 2:"Kedd", 4:"Csütörtök", 5:"Csütörtök" }     # Dictionary

# Adjunk hozzá egy új "szerda" elemet
my_dict[3] = "Szerda"                   # Hozzáadás

# Módosítsuk az 1-es kulcsú elemet "monday"-ra
my_dict[1] = "Monday"                   # Módosítás

# Vegyük ki azt az elemet, aminek a kulcsa 1
# print(my_dict[1])                       # A 1 nem index, hanem kulcs

# Elem kivétele kulcs alapján
# print(my_dict[0])                       # Hibát dobhat
print(my_dict.get(0))                     # None, ha nem létezik

# Töröljünk egy elemet (1-es kulcs)
del my_dict[1]

# Nyomtassuk ki a kulcsokat és értékeket
print(my_dict.keys())
print(my_dict.values())

# Print minden kulcsot
for value in my_dict.keys():
    print(value)

# Print minden értéket
for value in my_dict.values():
    print(value)

# Print minden értéket és kulcsot
for key, value in my_dict.items():
    print(key)
    print(value)