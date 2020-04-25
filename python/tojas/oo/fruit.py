class Fruit:
    name = ''
    calories = 0
    color = ''

    def __init__(self, name, calories, color):
        self.name = name
        self.calories = calories
        self.color = color

    def intro(self):
        print('Ez egy gyumolcs')
        print('a neve:', self.name)
        print('a szine:', self.color)
        print('a kaloria tartalma', self.calories)

    def norbi_update(self, minus):
        self.calories -= minus

    def __str__(self):
        return self.name


banan = Fruit('banana', 100, 'sarga')
banan.norbi_update(50)
banan.intro()
print(banan)