import sys
# Abszolút elérés (nem javasolt):
# sys.path.append("c:\\Users\\robert\\Documents\\00_Repositories\\http-courses\\python\\Riel\\03_ObjectOrientation\\")

# Relatív elérés:
# Mindig ahhoz a mappához képest kell megadni, amelyikből a programot futtatjuk.
# Ha a module mappából futtatjuk, akkor ".. kell, mert egyel fentebbi mappában keressük a student-et
# Ha a fentebbi mappából futtatjuk (amiben a student.py van), akkor csak "." kell (az aktuális mappára mutat) 
sys.path.append("..")

from student import Student

robert = Student("Robert", "férfi", 42)
print(robert)
