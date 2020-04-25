# Lista --------------------------------------------------
# Készítsünk egy Tuple objektumot
my_tuple = (1,2,3)
my_tuple = (1,"cica",3)

# Hozzunk létre egy új tuple-t, úgy, hogy a régihez hozzáadunk még elemeket
masodik_tuple = my_tuple + ("kutya", "birka")

# Számoljuk meg, hányszor van a "kutya" elem a tuple-ban
elofordulas = masodik_tuple.count("kutya")

# Hányadik indexen található a "kutya"?
elofordulas = masodik_tuple.index("kutya")

# my_tuple[0]  = "55"

print(elofordulas)

# Dictionary --------------------------------------------------
# Kulcs (key) - Elem (value)

# Készítsünk egy dictionary-t számozott szövegekkel
my_dict = {1:"Hétfő", 2:"kedd", 3:"szerda"}

# Módosítsuk az elsőt "monday"-ra
my_dict[1] = "Monday"
# ha új kulcsot adok meg, akkor az új elemet készít

# Töröljünk egy elemet
print(my_dict)                      # 3 elemünk van
item = my_dict.pop(2)               # Kiveszi és törli
print("Item pop-al: " + item)
print(my_dict)                      # 2 elemünk van
# del my_dict[2]                    # Csak törli

# Elem kivétele a listából
first = my_dict[1]                  # Hibára futhat
first = my_dict.get(1)              # None-t ad vissza, ha nincs elem a kulcson

# Nyomtassuk ki a kulcsokat és értékeket
print("Keys: ")
print(my_dict.keys())
print("Values: ")
print(my_dict.values())