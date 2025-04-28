"""
Student's Full Name
April 27, Functions
"""
#import math module 
import math

# Example 3
def greeting():
    print("Welcome to functions!")

# example 4, function with parameter 'username'
def printusername(username):
    print(f"Welcome to function {username}")

# example 5, function with default parameters
def user_country(username="(no name)", country="unknown country"):
    print(f"{username} is living in {country}")
    return

# example 6: function that returns a value
# function that takes two numbers and return the product of them
def product(n1=0, n2=1):
    return n1 * n2

# example 7: Boolean function
# function to check if a number is a multiple of 3
def multiple3(n):
    if n % 3 == 0:
        return True
    else:
        return False

# example 8: composition function
# define function to collect, validate, and return a number between 1 and 9
def collectnum():
    n = float(input("Enter a number between 1 and 9 (inclusive)"))
    # validate the number
    while (not (1 <= n <= 9)):
        n = float(input("Re-enter a number again: "))
    return n

def sumnumbers(totalnumbers):
    sum = 0
    for n in range(totalnumbers):
        sum += collectnum()  # composition function
    return sum

# function to print result
def printresult(totalsum):
    print(f"Sum of all numbers is = {totalsum}")


# example 9
# define a function to calculate and return the area of a circle
# formula = radius^2 * pi
def areacircle(radius):
    a = math.pow(radius, 2) * math.pi
    return round(a, 2)

# function to print result
def areaprint(area, radius=0):
    print(f"The area of a circle with {radius} radius is {area}")

# function to return the ratio of two numbers (hours)
def ration_hour(hour):
    dayhour = 24
    return hour / dayhour

# example 10: try-except
# function to return the ratio of two numbers (hours)
def ratio_hour(hour):
    try:
        dayhour = 24
        r = dayhour / hour
    except ZeroDivisionError:
        print('ZERO EXCEPTION')
        print("number can't be divided by zero")
        return 0
    except ValueError:
        print('VALUE EXCEPTION')
        print("Number was not provided")
        return 0
    except:
        print('GENERAL EXCEPTION')
        print("There was an error in the division")
    else:
        print('DIVISION IS FINE')
        return r
    finally:
        print("------ Process completed! --------")

# example 11
# defining a class name 'Myclass'
class Myclass:
    # property (attribute)
    id = 12345

    # method
    def msg(self):
        return "Welcome to Python class"

# example 12
class Complexnumber():
    # instantiate of the class
    def __init__(self, realnumber, imgnumber):
        self.r = realnumber
        self.i = imgnumber

# example 13
class Car:
    # instantiate of the class
    def __init__(self, make, model, year):
        self.carmake = make
        self.carmodel = model
        self.caryear = year

    # set property 'odometer'
    odometer_reading = 0

    # method to return descriptive of the car
    def get_car_description(self):
        return f"{self.carmake} with model {self.carmodel} was made on {self.caryear}"
    
    # method to read the odometer
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it"

    # method to update the odometer
    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Odometer CAN\'T roll back')

    # method to add miles into the odometer
    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading =+ miles
        else:
            print("Can't add negative miles")



#Lab 11, class in Python extra points assignment
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)
