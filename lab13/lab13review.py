"""
Daria Khotunitskaya
May 5, Python classes
"""
class Person:
    def __init__(self, name, age):
        self.username = name
        self.user_age = age
    def __str__(self):
        return f"Username={self.username} \nUser age = {self.user_age}"
    #method
    def intro(self):
        return f"Hello, I am {self.username}"

print("\n ---Example 1----")        
#create an object of the class
user1= Person("Peter", 23)
print(user1.intro())
              
# example 2, private properties
print("\n ---Example 2----")   
class Chair:
    #accesible properties
    chair_color= "brown"
    # initializing class properties
    def __init__(self, height, width, length):
        self.chairheight = height
        self.__width = width
        self.chairlength = length*2
    #method to pass length
    def pass_length(self):
        return self.chairlength
    #method to return volume
    def volume(self):
        return self.chairheight * self.__width * self.chairlength
    #method to return color
    def color(self):
        return self.chair_color  
    #method to return description of chair
    def description(self):
        return f"The total volume of the chair is {self.volume()} and the color is {self.chair_color}"
    #method with a private property
    def setprice(self,price):
        self._chairprice = price
    
# create an object
userchair1 = Chair(2,5,9)
print(f"The chair length is = {userchair1.chairlength}")
print(f"The chair width is = {userchair1._Chair__width}")

#call method pass length
print(f"The chair length is = {userchair1.pass_length()}")
print(f"The chair volume is = {userchair1.volume()}")
print(userchair1.description())

#call private method
userchair1.setprice(25)
print( f"The price of the chair is ${userchair1._chairprice}")