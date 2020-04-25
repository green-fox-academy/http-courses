class Fleet(object):
    def __init__(self):
        self.things = []

    def add(self, thing):
        self.things.append(thing)

    def __str__(self):
        result = ""
        for i, thing in enumerate(self.things):
            result += str(i+1) + ". " + str(thing) + "\n"
        return result