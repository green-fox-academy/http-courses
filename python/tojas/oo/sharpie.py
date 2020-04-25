class Sharpie:
    def __init__(self, color, width):
        self.color = color
        self.width = width
        self.ink_level = 100

    def use(self):
        self.ink_level -= 10