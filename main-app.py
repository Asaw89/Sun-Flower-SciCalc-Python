from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def displayResult(x: float):
    print(x, "\n")


def performCalcLoop(calc):
    while True:
        choice = input("What Do You Want? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'addition':
            a, b = getTwoNumbers()
            displayResult(calc.addition(a, b))
        elif choice == 'subtraction':
            a, b = getTwoNumbers()
            displayResult(calc.subtraction(a, b))
        elif choice == 'division':
            a, b = getTwoNumbers()
            displayResult(calc.division(a, b))
        elif choice == 'multiplication':
            a, b = getTwoNumbers()
            displayResult(calc.multiplication(a, b))
            
        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
