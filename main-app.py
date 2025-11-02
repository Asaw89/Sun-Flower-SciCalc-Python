from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input("first number? "))
    return a



def displayResult(x: float, display_mode="decimal"):
    # Convert the number based on the mode 
    if display_mode == "binary": 
        result = bin(int(x)) #converts to binary
    elif display_mode == "octal": 
        result = oct(int(x)) #coverts to octal
    elif display_mode == "hexadecimal":
        result = hex(int(x)) #coversts to hexadecimal
    else: #decimal - normal number 
        result = x 

    print(result, "\n")

#New! This function will change how numbers are displayed 
def switchDisplayMode(mode):
    return(mode)


def performCalcLoop(calc):
    state = 0 
    display_mode = "decimal" # New! This remembers which mode we're in 
    while True:
        print 
        choice = input("How can I Help You? (type 'display' to change mode) ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b), display_mode)
        elif choice == 'sub':
            a, b = getTwoNumbers()
            displayResult(calc.sub(a, b), display_mode)
        elif choice == 'div':
            a, b = getTwoNumbers()
            displayResult(calc.div(a, b), display_mode)
        elif choice == 'multi':
            a, b = getTwoNumbers()
            displayResult(calc.multi(a, b), display_mode)
        elif choice == 'square':
            a= getOneNumber()
            displayResult(calc.square(a), display_mode)
        elif choice == 'expo':
            a, b= getTwoNumbers()
            displayResult(calc.expo(a, b), display_mode)
        elif choice == 'inverse':
            a=getOneNumber()
            displayResult(calc.inverse(a), display_mode)

        #scientific funtions 
        elif choice == 'sin':
            a= getOneNumber()
            result = calc.sine(a)
            displayResult(result, display_mode)
        
        elif choice == 'cosine':
            a= getOneNumber()
            result = calc.cosine(a)
            displayResult(result, display_mode)

        elif choice == 'tangent':
            a= getOneNumber()
            result = calc.tangent(a)
            displayResult(result, display_mode)

        elif choice == 'display':
            print("Choose display mode")
            print("1. Binary")
            print("2. Octal")
            print("3. Decimal")
            print("4. Hexadecimal")
            mode_choice = input("Enter your choice: ")

            if mode_choice == '1':
                display_mode = switchDisplayMode("binary")
            elif mode_choice == '2': 
                display_mode = switchDisplayMode("octal") 
            elif mode_choice == '3':
                display_mode = switchDisplayMode("decimal")
            elif mode_choice == '4':
                display_mode = switchDisplayMode("hexadecimal")
            print(f"Debug: display_mode is now {display_mode}") #TEST DEBUG CODE 
        
                                             
        
            
        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
