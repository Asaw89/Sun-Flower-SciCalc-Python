class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return 0

# add lots more methods to this calculator class.
    def sine(self, x):
        if self.trig_units == "degrees":
            x = math.radians(x)
        return math.sin(x)