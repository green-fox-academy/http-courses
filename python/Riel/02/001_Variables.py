# Készítsünk egy változót minden nem-kollekció jellegű típushoz
# Printeljük a típusokat:

my_int = 6
my_float = 6.7
my_string = "Sziasztok"
my_boolean = True
my_nothing = None

# Printeljük a típusokat:
print(type(my_boolean))

# Adjunk össze két számot
a = 9
b = 6.1
result = a + b

# Vonjunk ki egymásból 2 számot
result = a - b

# Szorozzunk össze 2 számot
result = a * b

# Osszunk el egymással 2 számot
result = a / b 
result = a // b 

# Keressük meg az osztás utáni maradékot
result = 11 % 3             # modulo operátor

# Keressük meg 5 második hatványát
result = 5 ** 2

first_number = 10
second_number = 20
third_number = 20


# Kisebb, nagyobb, kisebb vagy egyenlő, nagyobb vagy egyenlő, egyenlő, nem egyenlő
result = first_number != second_number

# Írjuk ki, hogy "igaz" vagy "hamis", attól függően, hogy az első, vagy a második
# ágába lépünk be az elágazásnak:
a = 2
my_boolean = (a % 2 != 0)
if my_boolean:
    print("Igaz")
else:
    print("Hamis")

# Nyomtassuk ki hogy kisebb, nagyobb vagy egyenlő, attól függően, hogy a értéke hogyan vizsonyul 
# b értékéhez.
a =10
b = 100
c = 50

# if (a < b < c):
if ((a < b) and (b < c)):
    print("Első")
elif (a > b):
    print("Második")
else:
    print("Harmadik")

# Mit fognak eredményezni a következő (assignment) operátorok?
result = 50
result += 10
result = result + 10
result += 10
result -= 10
result *= 2
result /= 10
result //= 6
result = result // 6


print(result)
print(type(result))