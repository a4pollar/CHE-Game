from matplotlib.patches import Polygon
from numpy import float_, int_

import matplotlib.pyplot as plt

 
def plot_transformation(xys_original, xys_transformed):
    """
    Given two lists, containing only tuples of ints/floats representing two polygons,
    this function will plot both of them to visualize the transformation between the two.
    """
    # Check input
    if _is_invalid(xys_original) or _is_invalid(xys_transformed):
        return None

    # Create figure and reference to ax
    fig = plt.figure()
    ax = fig.gca()

    # Calculate plot limits
    lims = _get_lims(xys_original + xys_transformed)

    # Check get lim is not None, and that it has correct shape before unpacking
    if type(lims) is tuple and len(lims) == 2:
        x_lim, y_lim = lims
    else:
        return None

    # Set plot limits
    plt.xlim(x_lim[0], x_lim[1])
    plt.ylim(y_lim[0], y_lim[1])

    # Set aspect ratio between the x and y direction to be equal.
    ax.set_aspect('equal')

    # Create polygons
    original_shape = Polygon(xy=xys_original, fill=False)
    transformed_shape = Polygon(xy=xys_transformed, fill=False)

    # Color the polygons
    original_shape.set_color("r")
    transformed_shape.set_color("b")

    # Add polygons to figure
    ax.add_patch(original_shape)
    ax.add_patch(transformed_shape)

    # Add legend
    ax.legend(["Original", "Transformed"], ncol=2)

    # Add axis labels
    plt.xlabel("x")
    plt.ylabel("y")

    # Show figure
    fig.show()


def _get_lims(lst):
    """
    Calculates the maximum and minimum x and y values from
    a list of tuples of form [(x1, y1), (x2, y2), ...]
    """

    # Check input
    if _is_invalid(lst):
        return None

    # Separate the xs and ys
    x_vals = [x for x, _ in lst]
    y_vals = [y for _, y in lst]

    # Calculate min and max values
    x_min = min(x_vals)
    x_max = max(x_vals)
    y_min = min(y_vals)
    y_max = max(y_vals)

    # Create padding for x and y direction, a fraction of range in the values
    # Used to make sure nothing overlaps with the axes or the legend
    pad_x = 0.2 * (x_max - x_min)
    pad_y = 0.3 * (y_max - y_min)

    # Calculate the limits, by add/subtracting the padding from the min and max values
    x_lim = [x_min - pad_x, x_max + pad_x]
    y_lim = [y_min - pad_y, y_max + pad_y]

    return x_lim, y_lim


def _is_invalid(lst):
    """
    Checks whether the provided list is a list of tuples,
    where each tuple contains only ints or floats.
    """
    # Check for invalid type
    if type(lst) is not list:
        return True

    # Iterate through each entry in the list
    for xy in lst:
        # Ensure it's a tuple
        if type(xy) is not tuple:		    
            return True

        # Check that it only contains 2 values
        if len(xy) != 2:		
            return True

        # Check that values are either floats or ints
        if _is_not_a_number(xy[0]) or _is_not_a_number([xy[1]]):
            return True

    # If we get this far, then it means that the input is valid
    return False


def _is_not_a_number(n):
    """
    Checks whether the given variable is a valid number type.
    """
    if not (type(n) is not float or
            type(n) is not float_ or
            type(n) is not int or
            type(n) is not int_):
        return True
    else:
        return False
