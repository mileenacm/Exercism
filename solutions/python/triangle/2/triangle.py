"""Module to determine the type of a triangle based on its sides."""

def is_valid_triangle(sides):
    """Helper function to check if the given sides form a valid triangle."""
    side_a, side_b, side_c = sides
    
    if side_a == 0 or side_b == 0 or side_c == 0:
        return False
        
    if (side_a + side_b >= side_c) and (side_b + side_c >= side_a) and (side_a + side_c >= side_b):
        return True
        
    return False

def equilateral(sides):
    """Return True if the triangle is equilateral."""
    side_a, side_b, side_c = sides
    if not is_valid_triangle(sides):
        return False
    return side_a == side_b == side_c

def isosceles(sides):
    """Return True if the triangle is isosceles."""
    side_a, side_b, side_c = sides
    if not is_valid_triangle(sides):
        return False
    return (side_a == side_b) or (side_b == side_c) or (side_a == side_c)

def scalene(sides):
    """Return True if the triangle is scalene."""
    side_a, side_b, side_c = sides
    if not is_valid_triangle(sides):
        return False
    return side_a != side_b and side_a != side_c and side_b != side_c