# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
import math
import Image

xy_options = ["x", "y"]
function_options = [
    ["prod", 2],
    ["cos_pi", 1],
    ["sin_pi", 1],
    ["cube", 1],
    ["reverse", 1]
]

def build_random_function(min_depth, max_depth):
    """ Constructs a 'random' function with a depth between the provided min_depth and max_depth,
        with the functions 'prod', 'cos_pi', 'sin_pi', 'exp', and 'sqrt' and the variables 'x', 
        and 'y'. The output is a string. That will look something like: 
                        ["prod",["sin_pi",["x"]],["cos_pi",["x"]]]
        which is equivalent to the mathematical statement:
                                    sin(x * pi) * cos(x * pi)
    """
    if max_depth == 0 or (min_depth == 0 and randint(0,1) == 1):
        return [xy_options[randint(0,1)]]
    else: 
        selected_function = function_options[randint(0,4)]
        if selected_function[1] == 1:
            return [selected_function[0], build_random_function(min_depth - 1, max_depth - 1)]
        elif selected_function[1] == 2:
            return [selected_function[0], build_random_function(min_depth - 1, max_depth - 1), build_random_function(min_depth - 1, max_depth - 1)]

def evaluate_random_function(f, x, y):
    """ Evaluate the given function (f) for the inputs specified (x, y). If the function is 
        not recognized, it will return the input value of y
    """
    # if x and y are out of bounds, set them straight
    if x < 1.0 or x > 1.0: 
        x = x - float(int(x))
    if y < 1.0 or y > 1.0:
        y = y - float(int(y))

    if f[0] == "x":
        return x
    elif f[0] == "y":
        return y
    elif f[0] == "prod":
        return evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y)
    elif f[0] == "cos_pi":
        return math.cos(math.pi * evaluate_random_function(f[1], x, y))
    elif f[0] == "sin_pi":
        return math.sin(math.pi * evaluate_random_function(f[1], x, y))
    elif f[0] == "cube":
        return evaluate_random_function(f[1], x, y)**3.0
    elif f[0] == "reverse":
        return -evaluate_random_function(f[1], x, y)
    else:
        return y


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    """
    slope = (float(output_interval_end) - float(output_interval_start))/(float(input_interval_end) - float(input_interval_start))
    return slope * (val - float(input_interval_start)) + float(output_interval_start)

def generate_random_image(filename, min_depth, max_depth):

    red_ints = [randint(min_depth, max_depth), randint(min_depth, max_depth)]
    green_ints = [randint(min_depth, max_depth), randint(min_depth, max_depth)]
    blue_ints = [randint(min_depth, max_depth), randint(min_depth, max_depth)]

    #print str(red_ints) + " " + str(green_ints) + " " + str(blue_ints)

    red_function = build_random_function(min(red_ints), max(red_ints))
    green_function = build_random_function(min(green_ints), max(green_ints))
    blue_function = build_random_function(min(blue_ints), max(blue_ints))

    width = 350
    height = 350
    im = Image.new("RGB", (width, height))
    for i in range(width):
        for j in range(height):
            # scale the x and y values from i and j
            scaled_x = remap_interval(i, 0, 350, -1, 1)
            scaled_y = remap_interval(j, 0, 350, -1, 1)
            # set all of the pixel values
            red_pixel_value = evaluate_random_function(red_function, scaled_x, scaled_y)
            green_pixel_value = evaluate_random_function(green_function, scaled_x, scaled_y)
            blue_pixel_value = evaluate_random_function(blue_function, scaled_x, scaled_y)
            # put them in the image
            if red_pixel_value < -1 or red_pixel_value > 1: 
                print "Bad red pixel! -> " + str(red_pixel_value)
                print "\t" + str(red_function)
            if green_pixel_value < -1 or green_pixel_value > 1: 
                print "Bad green pixel! -> " + str(green_pixel_value)
                print "\t" + str(green_function)
            if blue_pixel_value < -1 or blue_pixel_value > 1: 
                print "Bad blue pixel! -> " + str(blue_pixel_value)
                print "\t" + str(blue_function)
            rgb_red_pixel_value = int(remap_interval(red_pixel_value, -1, 1, 0, 255))
            rgb_green_pixel_value = int(remap_interval(green_pixel_value, -1, 1, 0, 255))
            rgb_blue_pixel_value = int(remap_interval(blue_pixel_value, -1, 1, 0, 255))
            #print str(rgb_red_pixel_value) + " " + str(rgb_green_pixel_value) + " " + str(rgb_blue_pixel_value)
            im.putpixel([i, j], (rgb_red_pixel_value, rgb_green_pixel_value, rgb_blue_pixel_value))

    im.save(filename)

for i in range(5):
    generate_random_image("images/image" + str(i + 39) + ".jpg", 1, 10)






