#!/usr/bin/python3
"""Base Class"""
import json
import csv
import turtle


class Base:
    """This class is the “base” of all other classes in this project

    Returns:
        _type_: _description_
    """
    _nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id (ini, optional): instance id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            __class__._nb_objects += 1
            self.id = __class__._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries:

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: The JSON string representation of list_dictionaries:
        """
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): list of instances who inherits of Base
                example: list of Rectangle or list of Square instances
        """
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                listToSave = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(listToSave))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string

        Args:
            json_string (str): a string representing a list of dictionaries

        Returns:
            list: The list of the JSON string representation json_string
        """
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creae an instance with all attributes already set

        Args:
            **dictionary: dictionary with attributes to create the new instance
        Returns:
            object: An instance
        """
        if cls.__name__ == "Square":
            newShape = cls(1)
        elif cls.__name__ == "Rectangle":
            newShape = cls(1, 1)

        newShape.update(**dictionary)
        return newShape

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances:

        Returns:
            list: List of instances:
        """
        try:
            with open(f"{cls.__name__}.json", mode="r", encoding="utf-8") as f:
                objectsList = cls.from_json_string(f.read())
                return [cls.create(**obj) for obj in objectsList]

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to CSV file

        Args:
            list_objs (list): List of objects to be saved in CSV file
        """
        with open(f"{cls.__name__}.csv", mode="w", encoding="utf-8") as f:
            Writer = csv.writer(f, delimiter=",")
            if not list_objs:
                Writer.writerows([])
                return

            Writer.writerow(list_objs[0].to_dictionary().keys())
            for obj in list_objs:
                Writer.writerows([obj.to_dictionary().values()])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a CSV file and creates a new objects with its data

        Returns:
            list: list of objects created with data from the CSV file
        """
        try:
            with open(f"{cls.__name__}.csv", mode="r", encoding="utf-8") as f:
                reader = csv.reader(f, delimiter=",")

                rows = list(reader)
                dictKeys = tuple(rows[0])

                instances = []
                for row in rows[1:]:
                    dummyDict = {}
                    for i, value in enumerate(row):
                        dummyDict[dictKeys[i].lower()] = int(value)
                    instance = cls.create(**dummyDict)
                    instances.append(instance)

                return instances
        except FileNotFoundError:
            return []

    def draw(list_rectangles, list_squares):
        """Draws Rectangles and Squares

        Args:
            list_rectangles (list): a list of rectangles instances
            list_squares (list): a list of square instances
        """
        screen = turtle.Screen()
        screen.setup(1200, 720)
        t = turtle.Turtle()
        t.penup()
        t.goto(-turtle.window_width() / 2, turtle.window_height() / 2)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.pendown()

        max_height = 0

        t.color("red", "pink")
        for r in list_rectangles:
            t.begin_fill()
            t.forward(r.width)
            t.right(90)
            t.forward(r.height)
            t.right(90)
            t.forward(r.width)
            t.right(90)
            t.forward(r.height)
            t.right(90)
            t.end_fill()
            t.penup()
            t.forward(r.width + 50)
            t.pendown()
            max_height = r.height if r.height >= max_height else max_height

        t.penup()
        t.goto(-turtle.window_width() / 2, turtle.window_height() / 2)
        t.forward(50)
        t.right(90)
        t.forward(max_height + 100)
        t.left(90)
        t.pendown()

        t.color("green", "cyan")
        for s in list_squares:
            t.begin_fill()
            t.forward(s.size)
            t.right(90)
            t.forward(s.size)
            t.right(90)
            t.forward(s.size)
            t.right(90)
            t.forward(s.size)
            t.right(90)
            t.end_fill()
            t.penup()
            t.forward(s.size + 50)
            t.pendown()

        turtle.done()
