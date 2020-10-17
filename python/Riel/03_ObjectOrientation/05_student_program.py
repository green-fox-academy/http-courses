from student import Student

# print(Student.score)
# Ez nem elérhető osztály szinten
# print(Student.age)

robert = Student("Robert", "férfi", 42)
# robert.name = "Robert"
# robert.age = 42
# robert.gender = "ferfi"
# robert.score = 123
# robert.mood = "nagyon jó"
# print(robert)
anita = Student("Anita", "nő")
print("----------------")
anita.introduce()

robert.introduce()
robert.learn(30)
robert.introduce()

print(anita)
print(anita._score)

# Mégis el lehet érni:
# _object._class__variable
print(anita._Student__gender)