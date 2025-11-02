from calculator import Calculator

def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input("first number? "))
    return a



def displayResult(x: float):
    print()
    print(result, "\n")

def performCalcLoop(calc):
    state = 0
    last_result = None
    while True:
        print(state)
        choice = input("How can I Help You? (type 'display' to change mode) ")
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
        elif choice == 'mul':
            a, b = getTwoNumbers()
            displayResult(calc.mul(a, b))
        elif choice == 'square':
            a= getOneNumber()
            displayResult(calc.square(a))
        elif choice == 'expo':
            a, b= getTwoNumbers()
            displayResult(calc.expo(a, b))
        elif choice == 'inverse':
            a=getOneNumber()
            displayResult(calc.inverse(a))
        elif choice == 'squareroot':
            a=getOneNumber()
            displayResult(calc.squareroot(a))
       
        elif choice == '+':
             num = input()
             state = (calc.add(state, float(num)))
        elif choice == '-':
            num = input()
            state = (calc.sub(state, float(num)))
        elif choice == '/':
            num = input()
            state = (calc.div(state, float(num)))
        elif choice == '*':
            num = input()
            state = (calc.mul(state, float(num)))
        elif choice == '^':
            num = input()
            state = (calc.square(state, float(num)))
        elif choice == 'expo':
            a, b= getTwoNumbers()
            displayResult(calc.expo(a, b))
        elif choice == '-1':
            num = input()
            state = (calc.inverse(state, float(num)))
        elif choice == 'pow':
            a=getOneNumber()
            displayResult(calc.squareroot(state, float(num)))
        elif choice == 'clear':
            state = 0
        
        
        
            
        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
