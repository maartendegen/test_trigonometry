import numpy as np

print('Hello world')

def circum(radius):
	return 2*np.pi*radius

input_rad = float(input("Please give me the number of your circle:"))

print("The circumference of your circle is: ", circum(input_rad))


def area(radius):
	return np.pi*radius**2

print("The area of your circle is: ", area(input_rad))
