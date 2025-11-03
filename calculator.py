import math
class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return 0

    def inverse_sine(self, x):
        return math.asin(x)
    
    def inverse_cosine(self, x):
        return math.acos(x)
    
    def inverse_tangent(self, x):
        return math.atan(x)
    
    def factorial(self, x):
        return math.factorial(x)
    
    def switchUnitsMode(self, x):
        return 'switchUnitsMode'()
    
    def switchUnitsModeDelta(self, x):
        return 'switchUnitsModeDelta'(x)
    
# add lots more methods to this calculator class.
