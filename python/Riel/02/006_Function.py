# Készítsünk egy metódust print_value_and_type néven, ami ki tudja nyomtatni egy változó típusát
# Az eredmény legyen az alábbi formátumban:
# Az érték: 123, a típus: <class 'int'>
# Amennyiben a változó típusa None, csak ennyit nyomtasson:
# A változónak nincsen értéke

# A function definíciója:
def print_value_and_type(variable):
    if (variable == None):
        print("A változónak nincsen értéke")
    else:
        print("Az érték: " + str(variable) + ", a típus: " + str(type(variable)))

# A function meghívása:
print_value_and_type(None)




# Készítsünk egy metódust, ami visszaadja a leghosszabb szót egy mondatból, amit az megkap paraméterként
def get_longest_word(sentence):
    # 1. Split --> megkapjuk a szavak listáját
    words = sentence.split(" ")

    # 2. Végig megyek a listán, megszámolom minden szó hosszát és a leghosszabbat választom
    longest = words[0]
    for word in words:
        if (word == words[0]):
            continue

        if (len(word)>len(longest)):
            longest = word

    return longest


word = get_longest_word("Ez egy különösen hosszú mondat")
print(word)