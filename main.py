def print_balanced_equation():
    """
    Runs the chemical equation balance algorithm
    """
    print()
    user_input = input('Write the equation: ')
    try:
        equation = Equation(user_input)
        print('Balanced equation: ' + equation.balance())
        sleep(3)
        run_balance()
    except IndexError:
        print('Invalid input...')
        sleep(3)
        print_balanced_equation()


print('=================================================')
print('Insert chemical equation')
print('Example: H2 + O2 = H2O')
print_balanced_equation()
