#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square object.

        Args:
            size (int): the size of the Square instance
            x (int, optional): The x postion of the instance. Defaults to 0.
            y (int, optional): The y postion of the instance. Defaults to 0.
            id (id, optional): the id of the instance. Defaults to None.
        """
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter method

        Returns:
            int: The value of size
        """
        return self.width

    @size.setter
    def size(self, value):
        """size setter method

        Args:
            value (int): the new value of size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.

        Args:
            *args: A list of attributes to update.
            **kwargs: A dictionary of attributes to update.
        """
        try:
            if args:
                attrs = ("id", "size", "x", "y")
                for idx, arg in enumerate(args):
                    setattr(self, attrs[idx], arg)
            else:
                for key, value in kwargs.items():
                    setattr(self, key.lower(), value)
        except (IndexError, AttributeError):
            return

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.

        Returns:
            dict: The dictionary representation of a Square:
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
