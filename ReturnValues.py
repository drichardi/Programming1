#Return values
#Calling functions generates a return value
#which we usually assign to a variable to use as part
#of an expression

e = math.exp(1.0)
height = radius * math.sin(radians)

#The functions we have written the most are void, they have no return value;
#specifically their return value is None.

def area(radius):
    a = math.pi * radius ** 2
    return a
    
def area(radius):
    return math.pi * radius**2

#this is more concise, but often times temporary variables like a make a function more readable.
#we can have branches with multiple return statements

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
        
#only one runs
def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x
        
#does not handle when x = 0
#every possible path must hit a return statement

#INCREMENTAL DEVELOPMENT
#Pythagorean Theorem using (x1, y1) (x2, y2)
#distance formula google search for image
#what should this look like in python?
#outline
def distance(x1, y1, x2, y2):
    return 0.0
    
#not correct, but compiles and is testable
distance(1, 2, 4, 6) 
0.0 #3, 4, 5 triangle

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is', dx)
    print('dy is', dy)
    return 0.0
    #should get 3, 4

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    print('dsquared is: ', dsquared)
    return 0.0
    
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result
    
#does not display anything, just returns result
#our print statements were 'scaffolding' used to help test and develop
#INCREMENTAL
#1 Start with a working program and make small incremental changes. Makes finding errors easier.
#2 Use variables to hold intermediate values so you can display and check them
#3 Once the program is working, you may want to remove some scaffolding or consolidate multiple statements
#  into compound expressions, but only if it does not make the program difficult to read.

#make a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the lengths
#of the other two legs as arguements. Record each stage of the development process as you go.


#COMPOSITION
#calling functions from functions
#Write a function that takes 2 points, the center of a circle, 
#and a point on the perimeter of the circle, and computes the area of the circle
#Center point xc yc, perimeter xp, yp
#use distance
radius = distance(xc, yc, xp, yp)
result = area(radius)
#Encapsulate this working code into a function
def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result
    
#can be condensed to after debugging
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

       
