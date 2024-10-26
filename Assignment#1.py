#variables 
# Question no 1
# write a program that calculate the sum,difference,product and average of three numbers?
num1=25
num2=30
num3=35
print("SUM=",num1+num2+num3)         #SUM=90
print("DIFFERENCE=",num1-num2-num3)  #DIFFERENCE= -40
print("PRODUCT=",num1*num2*num3)     #PRODUCT= 26250
numbers=[25,30,35]
average=sum(numbers)/len(numbers)
print("AVERAGE=",average)                       #AVERAGE= 30.0

#Question no 2
# Write python code to calculate the area of the following shapes?
# area=21*base*height , area=side2 , Area=π×radius2 , Area=length×width

import math
# 1.area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height
base=5.5
height=8.5 
print("Area of Triangle:", area_triangle(base, height)) #Area of triangle = 23.375

# 2. Area of a Square
def area_square(side):
    return side ** 2
side=4
print("Area of Square:", area_square(side)) #Area of square = 16
    
# 3. Area of a Circle
def area_circle(radius):
    return math.pi * (radius ** 2)
radius=6.5
print("Area of Circle:", area_circle(radius)) #Area of circle = 132.73228961416876 

 # 4. Area of a Rectangle
def area_rectangle(length, width):
    return length * width
length=8
width=6
print("Area of Rectangle:", area_rectangle(length, width)) #Area of rectangle = 48

