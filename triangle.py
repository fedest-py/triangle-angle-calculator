#******************************************************************************
# triangle.py
#******************************************************************************
# Name: 
#******************************************************************************
# Remarks (optional):
#Eduardo Esteves
#MTH 3030
#

#ask for the sidelength values in descending order

print('''Please input the sidelengths of the triangle in descending oder (from biggest to smallest),
sidelengths can be equal to each other. Decimals are valid.''')

side_c = float(input('Enter length for side A (biggest value): '))

side_b = float(input('Enter length for side B:'))

side_a = float(input('Enter length for side C (smallest value): '))

import math

#use the law of cosines to find what the cos(x) (where x is the biggest angle) 
## is equal to

cos_x = ((side_c)**2 - (side_a)**2 - (side_b)**2)/(-2 * side_a * side_b)

#find value of angle x in cos(x) 

x = math.acos(cos_x)

#now use the law of sines to find what the sin(y) (where y is the medium angle)
## is equal to 

sin_y = (math.sin(x)/side_c)*side_b

y = math.asin(sin_y)

#now to find the last angle, z, by substraction 
# first we turn radians into degrees 

x = (x * 180)/math.pi

y = (y * 180)/math.pi

#now substract

z = 180 - x - y

#display message if the values are incorrect, display answer if all values are valid

if side_c <= 0:
    print('One or more values inputed are invalid')
elif side_b <= 0:
    print('One or more values inputed are invalid')
elif side_a <= 0:
    print('One or more values inputed are invalid')
elif side_c < side_b < side_a:
    print('Values must be entered in descending order')
else:
    print('Solved successfully!');print('The angles are:'); print(x); print(y); print(z)


