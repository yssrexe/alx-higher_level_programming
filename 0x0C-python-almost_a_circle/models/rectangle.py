#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
            x (int, optional): The x position of the Rectangle. Defaults to 0.
            y (int, optional): The y position of the Rectangle. Defaults to 0.
            id (int, optional): the id of the instance of Rectangle.
                                Defaults to None.
        """
        super().__init__(id)
        self._checkValue(width, "width")
        self._checkValue(height, "height")
        self._checkValue(x, "x")
        self._checkValue(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """The string representation of the class

        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def _checkValue(self, value, attrName):
        """check the type and value of the given value.

        Args:
            value (int): attribute value
            attrName (str): attribute name

        Raises:
            TypeError: <name of the attribute> must be an integer
            ValueError: <name of the attribute> must be >= 0
            ValueError: <name of the attribute> must be > 0
        """
        if type(value) is not int:
            raise TypeError(f"{attrName} must be an integer")

        if (attrName == "x" or attrName == "y") and value < 0:
            raise ValueError(f"{attrName} must be >= 0")
        elif (attrName == "width" or attrName == "height") and value <= 0:
            raise ValueError(f"{attrName} must be > 0")

    @property
    def width(self):
        """width getter method

        Returns:
            int: the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method

        Args:
            value (int): the new value for width
        """
        self._checkValue(value, "width")
        self.__width = value

    @property
    def height(self):
        """height getter method

        Returns:
            int: the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method

        Args:
            value (int): the new value for height
        """
        self._checkValue(value, "height")
        self.__height = value

    @property
    def x(self):
        """x getter method

        Returns:
            int: the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method

        Args:
            value (int): the new value for x
        """
        self._checkValue(value, "x")
        self.__x = value

    @property
    def y(self):
        """y getter method

        Returns:
            int: the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method

        Args:
            value (int): the new value for y
        """
        self._checkValue(value, "y")
        self.__y = value

    def area(self):
        """the area value of the Rectangle instance.

        Returns:
            int: the area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        print(self.y * "\n", end="")
        for _ in range(self.height):
            print(self.x * " ", end="")
            print(self.width * "#")

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute:"""
        try:
            if args:
                attrs = ("id", "width", "height", "x", "y")
                for idx, arg in enumerate(args):
                    setattr(self, attrs[idx], arg)
            else:
                for key, value in kwargs.items():
                    setattr(self, key.lower(), value)
        except (IndexError, AttributeError):
            return

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle

        Returns:
            dict: returns the dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
