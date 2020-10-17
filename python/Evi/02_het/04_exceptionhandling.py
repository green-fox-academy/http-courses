# Kivétel kezelés

# try

try:
    # megprobal valamit vegrehajtani
    pass
except Exception as e:
    # kezeli a kivetelt
    pass

# ha file-t akarunk megnyitni, a "FileNotFoundError"-ral keszulunk fel arra
# az esetre, hogy nincs ilyen file

try:
    file = open('hello.txt', 'r')
    print(file.readlines())
except FileNotFoundError as e:
    print('ilyen file nem letezik')
    print(e)
except Exception as e:
    print(e)

# NameError
try:
    hello = "hello"
    print(helo)
except NameError:
    print('nincs ilyen valtozo')

# IndexError

try:
    lista = [1, 2, 3]
    print(lista[8])
except IndexError:
    print('nincs ilyen indexu elem')
finally:
    print('vege a listaelemes muveleteknek')


# ZeroDivisionError
# print(1/0)

# else: try agban minden rendben ment
# finally: minden esetben lefut

print("file vege")
