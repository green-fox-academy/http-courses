class SharpieSet:
    def __init__(self):
        self.sharpies = []
    
    def add(self, sharpie):
        self.sharpies.append(sharpie)

    def count_usable(self):
        count = 0
        for sharpie in self.sharpies:
            if sharpie.ink_level > 0:
                count += 1
        return count

    def remove_trash(self):
        for i, sharpie in enumerate(self.sharpies):
            if sharpie.ink_level == 0:
                self.sharpies.pop(i)