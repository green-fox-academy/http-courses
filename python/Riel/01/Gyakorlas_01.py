# Melyek a Python nyelv fő jellemzői?
# Script, Interpreted, Object oriented, High-level, Dynamically typed, General-purpose

# Hogyan futtassam?
print("Sziasztok")

# Készítsünk egy változót minden nem-kollekció jellegű típushoz
# Printeljük a típusokat:

my_int = 5
my_float = 6.0
my_boolean = True
my_string = "Szöveg"
my_semmi = None

# print(type(my_int))
# print(type(my_float))
# print(type(my_boolean))
# print(type(my_string))
# print(type(my_semmi))


# Próbáljuk ki a leggyakoribb operátorokat:
# = --> érték adás

# Adjunk össze két számot
result = 3 + 7
result = 10 - 5
result = 10 * 5
result = 10 / 5
result = 10 // 7

# Keressük meg az osztás utáni maradékot
result = 11%3       # modulo

# Keressük meg 5 második hatványát
result = 5 ** 3

first_number = 10
second_number = 20
third_number = 20

# Kisebb, nagyobb, kisebb vagy egyenlő, nagyobb vagy egyenlő, egyenlő, nem egyenlő
# Azonosság
# result = first_number == second_number

# Nem azonosság
# result = first_number != second_number

# Írjuk ki, hogy "igaz" vagy "hamis", attól függően, hogy az első, vagy a második
# ágába lépünk be egy elágazásnak:

if (result % 2 == 0 or not result > 100):
    print("igaz")
else:
    print("hamis")

# Készítsünk elágazást, attól függően, hogy a második szám hogyan viszonyul az elsőhöz
if (second_number < first_number):
    print("nagyobb")
elif (first_number < second_number):
    print("kisebb")
else:
    print("egyenlő")

# Hogyan tudom a result változó értékét növelni hárommal?
result += 3

# Mit fognak eredményezni a következő (assignment) operátorok?
result = 50.5
# result += 10
# result -= 10
# result *= 3
# result /= 10
# result //= 2 


print(result)