from termcolor import colored
import math 

def Add(x, y):
    return x + y

def Sub(x, y):
    return x - y

def Mul(x, y):
    return x * y

def Div(x, y):
    return x / y

def Deg(x, y):
    return x ** y

def Calculations(choice_Selected):
    if choice_Selected == '+':
        while True:
            x = input('Enter first number\n===>')
            try:
                x = int(x)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            y = input('Enter second number\n===>')
            try:
                y = int(y)
            except:
                print('Please use numeric digits.')
                continue
            break
        print(colored("====> ", 'red') + colored( str(Add(x, y)),"yellow"))
    if choice_Selected == '-':
        while True:
            x = input('Enter first number\n===>')
            try:
                x = int(x)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            y = input('Enter second number\n===>')
            try:
                y = int(y)
            except:
                print('Please use numeric digits.')
                continue
            break
        print(colored("====> ", 'red') + colored( str(Sub(x, y)),"yellow"))
    if choice_Selected == '*':
        while True:
            x = input('Enter first number\n===>')
            try:
                x = int(x)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            y = input('Enter second number\n===>')
            try:
                y = int(y)
            except:
                print('Please use numeric digits.')
                continue
            break
        print(colored("====> ", 'red') + colored( str(Mul(x, y)),"yellow"))
    if choice_Selected == '/':
        while True:
            x = input('Enter first number\n===>')
            try:
                x = int(x)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            y = input('Enter second number\n===>')
            try:
                y = int(y)
            except:
                print('Please use numeric digits.')
                continue
            break
        print(colored("====> ", 'red') + colored( str(Div(x, y)),"yellow"))
    if choice_Selected == '**':
        while True:
            x = input('Enter first number\n===>')
            try:
                x = int(x)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            y = input('Enter Degree of 1st number\n===>')
            try:
                y = int(y)
            except:
                print('Please use numeric digits.')
                continue
            break
        print(colored("====> ", 'red') + colored( str(Deg(x, y)),"yellow"))
    if choice_Selected == 'x' or choice_Selected == 'X':
        exit

def perimeter_Circle(radius):
    print(colored("====> ", 'red') + colored( str(radius*2*3.1415) + "cm","yellow"))

def perimeter_Square(Side):
    print(colored("====> ", 'red') + colored( str(Side*4) + "cm","yellow"))

def perimeter_Rectangle(Length, Width):
    print(colored("====> ", 'red') + colored( str(2*(Length + Width)) + "cm","yellow"))

def perimeter_Parallelogram(side1, side2):
    print(colored("====> ", 'red') + colored( str(2*(side1+side2)) + "cm","yellow"))
    
def perimeter_Triangle(side1, side2, side3):
    print(colored("====> ", 'red') + colored( str(side1 + side2 + side3) + "cm","yellow"))

def perimeter_Regular_n_polygon(Number_of_Sides, Side):
    print(colored("====> ", 'red') + colored( str(Number_of_Sides * Side) + "cm","yellow"))

def perimeter_Trapezium(a, b, c, d):
    print(colored("====> ", 'red') + colored( str(a + b + c + d) + "cm", "yellow"))

def Perimeter(shape):
    if shape == '1':
        while True:
            Radius  = input("Enter the length of the Radius of the circle in cm\n====>")
            try:
                Radius = int(Radius)
            except:
                print('Please use numeric digits.')
                continue
            break
        perimeter_Circle(Radius)
    if shape == '2':
        while True:
            Side  = input("Enter the length of the Side of square in cm\n====>")
            try:
                Side = int(Side)
            except:
                print('Please use numeric digits.')
                continue
            break
        perimeter_Square(Side)
    if shape == '3':
        while True:
            Length  = input("Enter the length of Rectangle in cm\n====>")
            try:
                Length = int(Length)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            Width  = input("Enter the Width of Rectangle in cm\n====>")
            try:
                Width = int(Width)
            except:
                print('Please use numeric digits.')
                continue
            break
        perimeter_Rectangle(Length, Width)
    if shape == '4':
        while True:
            Side1  = input("Enter the length of first side in cm\n====>")
            try:
                Side1 = int(Side1)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            Side2  = input("Enter the length of side adjacent to the first side in cm\n====>")
            try:
                Side2 = int(Side2)
            except:
                print('Please use numeric digits.')
                continue
            break
        perimeter_Parallelogram(Side1, Side2)
    if shape == '5':
        while True:
            Side1  = input("Enter the length of first side of the triangle in cm\n====>")
            try:
                Side1 = int(Side1)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            Side2  = input("Enter the length of second side of the triangle in cm\n====>")
            try:
                Side2 = int(Side2)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            Side3  = input("Enter the length of third side of the triangle in cm\n====>")
            try:
                Side3 = int(Side3)
            except:
                print('Please use numeric digits.')
                continue
            break
        perimeter_Triangle(Side1, Side2, Side3)
    if shape == '6':
        while True:
            Number_of_Sides  = input("Enter the number of sides of the polygon \n====>")
            try:
                Number_of_Sides = int(Number_of_Sides)
            except:
                print('Please use numeric digits.')
                continue
            if Number_of_Sides < 3:
                print('Minimum sides of the polygon is 3')
                continue
            break
        while True:
            Side  = input("Enter the length of the side of the polygon in cm\n====>")
            try:
                Side = int(Side)
            except:
                print('Please use numeric digits.')
                continue
            break
        perimeter_Regular_n_polygon(Number_of_Sides, Side)
    if shape == '7':
        while True:
            a  = input("Enter the length of first side of the Trapezium in cm \n====>")
            try:
                a = int(a)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            b = input("Enter the length of the second side of the Trapezium in cm\n====>")
            try:
                b = int(b)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            c = input("Enter the length of the third side of the Trapezium in cm\n====>")
            try:
                c = int(c)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            d = input("Enter the length of the fourth side of the Trapezium in cm\n====>")
            try:
                d = int(d)
            except:
                print('Please use numeric digits.')
                continue
            break
        perimeter_Trapezium(a, b, c, d)

def Area_Circle(radius):
    print(colored("====> ", 'red') + colored( str(3.1415 * radius**2) + "cm","yellow"))

def Area_Square(Side):
    print(colored("====> ", 'red') + colored( str(Side**2) + "cm²","yellow"))

def Area_Rectangle(Length, Width):
    print(colored("====> ", 'red') + colored( str(Length * Width) + "cm²","yellow"))

def Area_Parallelogram(Base, Height):
    print(colored("====> ", 'red') + colored( str(Base * Height) + "cm²","yellow"))
    
def Area_Triangle(Base, Height):
    print(colored("====> ", 'red') + colored( str(Base * Height /2) + "cm²","yellow"))

def Area_Regular_n_polygon(Number_of_Sides, Side):
    x = 3.1415/ Number_of_Sides
    angle = 1/math.tan(x)
    print(colored("====> ", 'red') + colored( str(round(1/4*Number_of_Sides* (Side**2)*angle,2)) + "cm²","yellow"))

def Area_Trapezium(a, b, Height):
    print(colored("====> ", 'red') + colored( str(Height*(a + b)/2) + "cm²", "yellow"))

def Area(shape):
    if shape == '1':
        while True:
            Radius  = input("Enter the length of the Radius of the circle in cm\n====>")
            try:
                Radius = int(Radius)
            except:
                print('Please use numeric digits.')
                continue
            break
        Area_Circle(Radius)
    if shape == '2':
        while True:
            Side  = input("Enter the length of the Side of square in cm\n====>")
            try:
                Side = int(Side)
            except:
                print('Please use numeric digits.')
                continue
            break
        perimeter_Square(Side)
    if shape == '3':
        while True:
            Length  = input("Enter the length of Rectangle in cm\n====>")
            try:
                Length = int(Length)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            Width  = input("Enter the Width of Rectangle in cm\n====>")
            try:
                Width = int(Width)
            except:
                print('Please use numeric digits.')
                continue
            break
        perimeter_Rectangle(Length, Width)
    if shape == '4':
        while True:
            Base  = input("Enter the length of Base of the parallelogram in cm\n====>")
            try:
                Base = int(Base)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            Height  = input("Enter the length of Height of the parallelogram in cm\n====>")
            try:
                Height = int(Height)
            except:
                print('Please use numeric digits.')
                continue
            break
        Area_Parallelogram(Base, Height)
    if shape == '5':
        while True:
            Base  = input("Enter the Base of the triangle in cm\n====>")
            try:
                Base = int(Base)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            Height = input("Enter the Height of the triangle in cm\n====>")
            try:
                Height = int(Height)
            except:
                print('Please use numeric digits.')
                continue
            break
        Area_Triangle(Base, Height)
    if shape == '6':
        while True:
            Number_of_Sides  = input("Enter the number of sides of the polygon \n====>")
            try:
                Number_of_Sides = int(Number_of_Sides)
            except:
                print('Please use numeric digits.')
                continue
            if Number_of_Sides < 3:
                print('Minimum sides of the polygon is 3')
                continue
            break
        while True:
            Side  = input("Enter the length of the side of the polygon in cm\n====>")
            try:
                Side = int(Side)
            except:
                print('Please use numeric digits.')
                continue
            break
        Area_Regular_n_polygon(Number_of_Sides, Side)
    if shape == '7':
        while True:
            a  = input("Enter the length of first base of the Trapezium in cm \n====>")
            try:
                a = int(a)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            b = input("Enter the length of the second base of the Trapezium in cm\n====>")
            try:
                b = int(b)
            except:
                print('Please use numeric digits.')
                continue
            break
        while True:
            Height = input("Enter the length of the Height of the Trapezium in cm\n====>")
            try:
                Height = int(Height)
            except:
                print('Please use numeric digits.')
                continue
            break
        Area_Trapezium(a, b, Height)

def Volume_Cube(Side):
    print(colored("====> ", 'red') + colored( str(Side**3) + "cm³","yellow"))

def Volume_Cuboid(Side1, Side2, Side3):
    print(colored("====> ", 'red') + colored( str(Side1 * Side2 * Side3) + "cm³","yellow"))

def Volume_Sphere(Radius):
    print(colored("====> ", 'red') + colored( str(4/3*(3.1415 * Radius**3)) + "cm³","yellow"))

def Volume_HemiSphere(Radius):
    print(colored("====> ", 'red') + colored( str(2/3*(3.1415 * Radius**3)) + "cm³","yellow"))

def Volume_Cone(Radius, Height):
    print(colored("====> ", 'red') + colored( str(1/3*(3.1415 * Radius**2 * Height)) + "cm³","yellow"))

def Volume_Cylinder(Radius, Height):
    print(colored("====> ", 'red') + colored( str(3.1415 * Radius**2 * Height) + "cm³","yellow"))  

def Volume(Shape):
    if Shape == '1':
        while True:
            Side  = input("Enter the length of the Side of the Cube in cm\n====>")
            try:
                Side = int(Side)
            except:
                print('Please use numeric digits.')
                continue
            break        
        Volume_Cube(Side)
    if Shape == '2':
        while True:
            Side1  = input("Enter the length of the First Side of the Cuboid in cm\n====>")
            try:
                Side1 = int(Side1)
            except:
                print('Please use numeric digits.')
                continue
            break        
        while True:
            Side2  = input("Enter the length of the Second Side of the Cuboid in cm\n====>")
            try:
                Side2 = int(Side2)
            except:
                print('Please use numeric digits.')
                continue
            break        
        while True:
            Side3  = input("Enter the length of the Third Side of the Cuboid in cm\n====>")
            try:
                Side3 = int(Side3)
            except:
                print('Please use numeric digits.')
                continue
            break        
        Volume_Cuboid(Side1, Side2, Side3)
    if Shape == '3':
        while True:
            Radius  = input("Enter the length of the Radius of the Sphere in cm\n====>")
            try:
                Radius = int(Radius)
            except:
                print('Please use numeric digits.')
                continue
            break        
        
        Volume_Sphere(Radius)
    if Shape == '4':
        while True:
            Radius  = input("Enter the length of the Radius of the Hemi Sphere in cm\n====>")
            try:
                Radius = int(Radius)
            except:
                print('Please use numeric digits.')
                continue
            break        
        
        Volume_HemiSphere(Radius)
    if Shape == '5':
        while True:
            Radius  = input("Enter the length of the Radius of the Cone in cm\n====>")
            try:
                Radius = int(Radius)
            except:
                print('Please use numeric digits.')
                continue
            break        
        while True:
            Height  = input("Enter the length of the Height of the Cone in cm\n====>")
            try:
                Height = int(Height)
            except:
                print('Please use numeric digits.')
                continue
            break        
        Volume_Cone(Radius, Height)
    if Shape == '6':
        while True:
            Radius  = input("Enter the length of the Radius of the Cylinder in cm\n====>")
            try:
                Radius = int(Radius)
            except:
                print('Please use numeric digits.')
                continue
            break        
        while True:
            Height  = input("Enter the length of the Height of the Cylinder in cm\n====>")
            try:
                Height = int(Height)
            except:
                print('Please use numeric digits.')
                continue
            break        
        Volume_Cylinder(Radius, Height)
        