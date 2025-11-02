class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y
    
    def div(self, x, y):
        if y == 0:
            return ("error")
            return x / y
    
    def mul(self, x, y):
        return x * y
    
    def square(self, x):
        return x * x
    
    def expo(self, x, y):
        return x ** y
    
    def inverse(self, x):
        return 1/x
    
    def squareroot(self, x):
        if x < 0:
            return ("error")
        return pow(x, 0.5)
    
    def clear():
        return 0

# add lots more methods to this calculator class.
