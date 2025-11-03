from calculator import Calculator
from customFeaturs import CustomFeatures


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def displayResult(x: float):
    print(x, "\n")

def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'asin':
            num = input("Enter a nunber for inverse sine")
            result = calc.inverse_sine(float(num))
            print(result)

def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'math.factorial':
            num = input("Enter a nunber for inverse sine")
            result = calc.factorial(float(num))
            print(result)


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
