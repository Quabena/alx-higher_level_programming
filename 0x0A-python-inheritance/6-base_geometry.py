#!/usr/bin/python3

class BaseGeometry:
    """
    A class named BaseGeometry that serves as a base for geometric shapes.
    """

    def area(self):
        """
        Calculates the area of the geometric shape.
 
        Raises:
            Exception: This method is not implemented for the base class.
        """
        raise Exception("area() is not implemented")
