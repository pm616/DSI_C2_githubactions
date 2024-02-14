import math

#  Formula for area of a square: side_length ** 2

def calc_area_rectangle(side1_length, side2_length):
    if side1_length == side2_length:
        return side1_length ** 2
    else:
        return side1_length * side2_length




# square
def calc_area_square(side_lenghth):
    return side_lenghth ** 2

input_number = 2
output_number = calc_area_square(input_number)
print(f'cal_area_square({input_number})={output_number}')







# circle
import math
def calc_area_circle(radius):
    if not isinstance(radius, (float, int)):
        raise TypeError(f'radius is {radius} but should be a number')
    if radius < 0:
        raise ValueError(f'radius is {radius} but must be positive')
    return math.pi * radius ** 2