from termcolor import colored
from functions import * 
print(colored("<========== This calculator was made by Rudra Gupta ==========>"))

Name = input(colored("What is your name?\n====>", 'blue'))



while True:    
    while True:
        print(colored("Hi " + Name + ",\n1 = Arithmetic calculation\n2 = Perimeter and area calculation\n3 = Volume calculation\n4 to exit", 'green'))

        value = input('===>')
        if value == '1' or value == '2' or value == '3' or value == '4':
            break
        else :
            print('eneter correct value')
            continue
    if value == '1':
        while True:
            print(colored('<======== Arithmetic Calculations ========>','red'))
            while True:
                choice = print(colored(' Enter\n + for addition\n - for subtraction\n * for multiplication\n / for division\n ** for degree\n x to exit', 'blue'))
                print(' Enter your choice')
                choice_Selected = input("====>")
                if choice_Selected == '+' or choice_Selected == '-' or choice_Selected == '*' or choice_Selected == '/' or choice_Selected == '%' or choice_Selected == '**' or choice_Selected == 'x' or choice_Selected == 'X':
                    break
                else: 
                    print('Enter correct operator')
                    continue
            if choice_Selected == 'x' or choice_Selected == 'X':
                break
            Calculations(choice_Selected)
    if value == '2':
        while True:
            print(colored('<======== Perimeter and Area Calculation ========>','red'))
            while True:
                choice = print(colored(' Enter\n 1 for Perimeter\n 2 for Area\n 3 to Exit','blue'))
                print(' Enter your choice')
                choice_Selected = input("====>")
                if choice_Selected == '1' or choice_Selected == '2' or choice_Selected == '3':
                    break
                else: 
                    print('Enter correct option')
                    continue
            if choice_Selected == '1':
                print(colored('<======== Perimeter Calculation ========>','blue'))
                while True:
                    print(colored('Choose a shape\n1 = Circle\n2 = Square\n3 = Rectangle\n4 = Parallelogram\n5 = Triangle\n6 = Regular n-polygon\n7 = Trapezium\n8 = exit','blue'))
                    shape = input("===>")
                    if shape == '1' or shape == '2' or shape == '3' or shape == '4' or shape == '5' or shape == '6' or shape == '7' or shape == '8':
                        break
                    else: 
                        print('Enter correct option')
                        continue
                if shape == '8':
                    break
                Perimeter(shape)
            if choice_Selected == '2':
                print(colored('<======== Area Calculation ========>','blue'))
                while True:
                    print(colored('Choose a shape\n1 = Circle\n2 = Square\n3 = Rectangle\n4 = Parallelogram\n5 = Triangle\n6 = Regular n-polygon\n7 = Trapezium\n8 = exit','blue'))
                    shape = input("===>")
                    if shape == '1' or shape == '2' or shape == '3' or shape == '4' or shape == '5' or shape == '6' or shape == '7' or shape == '8':
                        break
                    else: 
                        print('Enter correct option')
                        continue
                if shape == '8':
                    break
                Area(shape)
            elif choice_Selected == '3':
                print('<===== Exit =====>')
                break
    if value == '3':
            while True:
                print(colored('<======== volume Calculation ========>','red'))
                while True:
                    choice = print(colored(' Enter\n 1 for Volume\n 2 to Exit','blue'))
                    print(' Enter your choice')
                    choice_Selected = input("====>")
                    if choice_Selected == '1' or choice_Selected == '2':
                        break
                    else: 
                        print('Enter correct option')
                        continue
                if choice_Selected == '1':
                    while True:
                        print(colored('Choose a shape\n1 = Cube\n2 = Cuboid\n3 = Sphere\n4 = Hemi Sphere\n5 = Cone\n6 = Cylinder\n7 = exit','blue'))
                        shape = input("===>")
                        if shape == '1' or shape == '2' or shape == '3'or shape == '4' or shape == '5' or shape == '6' or shape == '7':
                            break
                        else:
                            print('Enter correct shape number')
                            continue

                    if shape == '7':
                        break
                    Volume(shape)
                    
                if choice_Selected == '2':
                    break
    if value == '4':
        break