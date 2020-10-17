# https://docs.python.org/3/library/exceptions.html


try:
    print("1")
    # print(55/0)
    print("2")
    # file = open("nemletezik.txt")
    print("3")
except ZeroDivisionError:       # tetszőleges
    print("Nullával nem kellene osztani")
except FileNotFoundError as e:
    print("A file nem található")
    print(e)
except:  # csak egy
    print("Valami hiba törpént")
else:   # csak akkor hívódik, ha nem történt hiba
    print("nem volt hiba")
finally:
    print("mindig meghívódik")