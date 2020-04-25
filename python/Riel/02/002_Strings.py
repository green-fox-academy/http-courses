str1, str2 = "Ungváli", "Péter"

# Fűzzük egybe a két string-et egy szóközzel együtt
name = str1 + " " + str2

# Adjuk hozzá, hogy "ma sajnos nincs jelen"
name += " ma sajnos nincs jelen"

# Nyerjük ki az első és utolsó elemét
first = name[0]
last = name[-1]
last = name[len(name)-1]

# Hogyan tudjuk meg, milyen hosszú a szöveg?
hossz = len(name)

# Módosítsuk az üzenetet (Ungvári a helyes)
name = name.replace("Ungváli", "Ungvári")

# Gyűjtsük ki az összes szót egy listába
characters = name.split(' ')

