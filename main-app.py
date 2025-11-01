from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input("first number? "))
    return a



def displayResult(x: float):
    print(x, "\n")


def performCalcLoop(calc):
    state = 0 
    while True:
        print 
        choice = input("How can I Help You? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))
        elif choice == 'sub':
            a, b = getTwoNumbers()
            displayResult(calc.sub(a, b))
        elif choice == 'div':
            a, b = getTwoNumbers()
            displayResult(calc.div(a, b))
        elif choice == 'multi':
            a, b = getTwoNumbers()
            displayResult(calc.multi(a, b))
        elif choice == 'square':
            a= getOneNumber()
            displayResult(calc.square(a))
        elif choice == 'expo':
            a, b= getTwoNumbers()
            displayResult(calc.expo(a, b))
        elif choice == 'inverse':
            a=getOneNumber()
            displayResult(calc.inverse(a))
        
            
        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
