class Student:
    # tagváltozók értékekkel
    # name =""
    # age = 0
    # gender = ""
    # score = 0

    # https://www.tutorialsteacher.com/python/private-and-protected-access-modifiers-in-python

    def __init__ (self, name, gender, age=0):
        self.name = name
        self.age = age
        # private szándék jelölés __
        # AttributeError - közvetlen elérésnél
        # más szintaxissal továbbra is elérhető
        self.__gender = gender
        # protected szádék jelölés _
        self._score = 0


    def __str__ (self):
        return "Sziasztok, az én nevem: " + self.name

    def introduce(self):        # convenció : self
        print (self.name + ", " + str(self.age) + ", " + str(self._score) + ", " + self.__gender)
    
    def learn(self, point):
        self._score += point