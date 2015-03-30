# chris beck's function builder thing
import random
from PIL import Image
from math import pi, cos, sin, sqrt

"""General Comments: Overall nice job. Make sure you work on adding tests and comments. You're getting a lot better on keeping your
code clear and concise, I can see some great improvements with that! I'm a little confused why you rewrote the function paul wrote
for remap interval though...it seems a little sketch with all the float conversions(see my comments on how this may be sketchily fixing
a mistake that may actually stem from somewhere else). Overall though nice! (Next time though, check the grading instructions, because
you were also supposed to include two generated art images with this. Don't worry about it this time, it wasn't hard for me to
generate some from your code, but check for next time.)
"""

def create_function(depth):
    if depth == 0:
        return random.choice(["x", "y"])
    choice = random.choice(["sin","cos","prod","avg", "cube", "root"])
    if choice == "sin":
        return ["sin", create_function(depth-1)]
    elif choice == "cos":
        return ["cos", create_function(depth-1)]
    elif choice == "prod":
        return ["prod", create_function(depth-1), create_function(depth-1)]
    elif choice == "avg":
        return ["avg", create_function(depth-1), create_function(depth-1)]
    elif choice == "cube":
        return ["cube", create_function(depth-1)]
    elif choice == "root":
        return ["root", create_function(depth-1)]
    #Nice, and concise. Good job. 
    #By using the build_random_function below, you are easily able to choose a random depth between min and max. This was a common bug some people missed.
    #However, add some tests and description of this function!


def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
    at most max_depth (see assignment writeup for definition of depth
    in this context)
    min_depth: the minimum depth of the random function
    max_depth: the maximum depth of the random function
    returns: the randomly generated function represented as a nested list
    (see assignment writeup for details on the representation of
    these functions)
    """

    depth = random.randint(min_depth,max_depth)
    return create_function(depth)


def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
    Representation of the function f is defined in the assignment writeup
    f: the function to evaluate
    x: the value of x to be used to evaluate the function
    y: the value of y to be used to evaluate the function
    returns: the function value
    >>> evaluate_random_function(["x"],-0.5, 0.75)
    -0.5
    >>> evaluate_random_function(["y"],0.1,0.02)
    0.02
    """

    if f[0] == "x":
        return x
    elif f[0] == "y":
        return y 
    elif f[0] == "sin":
        return sin(pi * evaluate_random_function(f[1], x, y))
    elif f[0] == "cos":
        return cos(pi * evaluate_random_function(f[1], x, y))
    elif f[0] == "prod":
        return evaluate_random_function(f[1], x, y) * evaluate_random_function(f[1], x, y)
    elif f[0] == "avg":
        return 0.5 * (evaluate_random_function(f[1], x, y) + evaluate_random_function(f[1], x, y))
    elif f[0] == "cube":
        return evaluate_random_function(f[1], x, y)**3
    elif f[0] == "root":
        return sqrt(abs(evaluate_random_function(f[1], x, y)))

    #good catch on making sure you included the absolute value for root. Clear and concise. Once again, add tests.

# eq = build_random_function(7,9)
# print eq
# print evaluate_random_function(eq,20,30)

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
    input_interval_end], return an output value scaled to fall within   
    the output interval [output_interval_start, output_interval_end].
    val: the value to remap
    input_interval_start: the start of the interval that contains all
    possible values for val
    input_interval_end: the end of the interval that contains all possible
    values for val
    output_interval_start: the start of the interval that contains all
    possible output values
    output_inteval_end: the end of the interval that contains all possible
    output values
    returns: the value remapped from the input to the output interval
    >>> remap_interval(0.5, 0, 1, 0, 10)
    5.0
    >>> remap_interval(5, 4, 6, 0, 2)
    1.0
    >>> remap_interval(5, 4, 6, 1, 2)
    1.5
    """
    outend = float(output_interval_end) #Sidenote: having to covert all these to floats seems kind of sketch. 
    # There shouldn't have been a problem with the function Paul already wrote for you... 
    # it seems like you're trying to fix an issue with your code in the wrong way here. 
    # If the code was giving you issues, the right place to fix what caused the float problem in the functions 
    # you wrote, not this one.

    outstart = float(output_interval_start)
    inend = float(input_interval_end)
    instart = float(input_interval_start)

    output_range = outend - outstart
    input_range = inend - instart

    in_value = val - input_interval_start

    percent_value = in_value/input_range   

    percent_out_value = output_range * percent_value

    return percent_out_value + output_interval_start

    # Did you write this function on your own? Wasn't it already included in the assignment? as:

    # ratio_input = (val - input_interval_start)/float(input_interval_end - input_interval_start)
    # scaled_number = (ratio_input*float(output_interval_end - output_interval_start)) + output_interval_start
    # return scaled_number



def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
    use as an RGB color code.
    val: value to remap, must be a float in the interval [-1, 1]
    returns: integer in the interval [0,255]
    >>> color_map(-1.0)
    0
    >>> color_map(1.0)
    255
    >>> color_map(0.0)
    127
    >>> color_map(0.5)
    191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.
    filename: string filename for image (should be .png)
    x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255), # Red channel
                            random.randint(0, 255), # Green channel
                            random.randint(0, 255)) # Blue channel
    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.
    filename: string filename for image (should be .png)
    x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(7,9)
    green_function = build_random_function(7,9)
    blue_function = build_random_function(7,9)
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                        color_map(evaluate_random_function(red_function, x, y)),
                        color_map(evaluate_random_function(green_function, x, y)),
                        color_map(evaluate_random_function(blue_function, x, y))
                        )
    im.save(filename)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
# Create some computational art!
# TODO: Un-comment the generate_art function call after you
# implement remap_interval and evaluate_random_function
generate_art("myart.png")
# Test that PIL is installed correctly
# TODO: Comment or remove this function call after testing PIL install
#test_image("noise.png")