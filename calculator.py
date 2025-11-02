class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y
    
    def div(self, x, y):
        return x / y
    
    def multi(self, x, y):
        return x * y
    
    def square(self, x):
        return x * x
    
    def expo(self, x, y):
        return x ** y
    
    def inverse(self, x):
        return 1/x

# add lots more methods to this calculator class.
    def sine(self, x):
        if self.trig_units == "degrees":
            x = math.radians(x)
        return math.sin(x)
    
    def cosine(self,x):
        if self.trig_units == "degrees":
            x = math.radians(x)
        return math.cosine(x)
    
    def tangent(self, x):
        if self.trig_units == "degrees":
            x = math.radians(x)
        return math.tan(x)
    