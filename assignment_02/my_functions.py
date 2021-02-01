# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Alexander Gomez
#
# Date: 1/31/21
# 
##################################################
#
# Sample Script for Assignment 2: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module


##################################################
# Function Definitions
##################################################

# Exercise 1

def average(num1: float, num2: float) -> float:
    """Return the average of num1 and num2.

    >>> average(10,20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    >>> average(5,10)
    7.5
    """

    return (num1 + num2) / 2

print(average(10,20))

print(average(2.50,3.0))

print(average(5,10))


# Define the rest of your functions for Exercises 2-6.

# Exercise 2

def area_of_circle(r: float) -> float:
    """Return the area of a circle with radius r.
    >>>(area_of_circle(1))
    3.14
    >>>(area_of_circle(2))
    12.56
    >>>(area_of_circle(3))
    28.26
    """
    return ((3.14)*r**2)

print(area_of_circle(1))

print(area_of_circle(2))

print(area_of_circle(3))

# Exercise 3

def volume_of_cylinder(r: float, h: float) -> float:
    """Return the volume of a cylinder radius r and height h.
    >>> volume_of_cylinder(2,5)
    62.80
    >>> volume_of_cylinder(3,2)
    56.52
    >>> volume_of_cylinder(1,4)
    12.56
    """
    
    return area_of_circle(r)*h

print(volume_of_cylinder(2,5))

print(volume_of_cylinder(3,2))

print(volume_of_cylinder(1,4))

def utility(x: float, y: float, a: float) -> float:
    """Return the utility value from the Cobb-Douglas utility function.
    >>> utility(2,3,2)
    1.33
    >>> utility(1,5,3)
    0.04
    >>> utility(3,1,4)
    81.0
    """
    return x**a*y**(1-a)

print(utility(2,3,2))

print(utility(1,5,3))

print(utility(3,1,4))


    
    
    
    






##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results. 


print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating average(10,20)")
print("Expected: " + str(15.0))
print("Got: " + str(average(10,20)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating average(2.5, 3.0)")
print("Expected: " + str(2.75))
print("Got: " + str(average(2.5, 3.0)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating average(5,10)")
print("Expected: " +str(7.5))
print("Got: " + str(average(5,10)))

######################################################

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating area_of_circle(1)")
print("Expected: " + str(3.14))
print("Got: " + str(area_of_circle(1)))

print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating area_of_circle(2)")
print("Expected: " + str(12.56))
print("Got: " + str(area_of_circle(2)))

print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating area_of_circle(3)")
print("Expected: " + str(28.26))
print("Got: " + str(area_of_circle(3)))

##############################################################################

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")
 
print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating volume_of_cylinder(2,5)")
print("Expected: "+ str(62.80))
print("Got:" + str(volume_of_cylinder(2,5)) )

print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating volume_of_cylinder(3,2)")
print("Expected: "+ str(56.52))
print("Got:" + str(volume_of_cylinder(3,2)) )

print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating volume_of_cylinder(1,4)")
print("Expected: "+ str(12.56))
print("Got:" + str(volume_of_cylinder(1,4)) )

######################################################

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating utility(2,3,2)")
print("Expected: "+ str(1.33))
print("Got:" + str(utility(2,3,2)))

print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating utility(1,5,3)")
print("Expected: "+ str(0.04))
print("Got:" + str(utility(1,5,3)))

print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating utility(3,1,4)")
print("Expected: "+ str(81.0))
print("Got:" + str(utility(3,1,4)))




# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


##################################################
# End
##################################################