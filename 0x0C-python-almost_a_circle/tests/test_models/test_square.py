#!/usr/bin/python3
"""Unitests for Square class"""
import unittest
from pathlib import Path
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """..."""

    def test_two_valid_args(self):
        """..."""
        square = Square(12, 44)
        self.assertEqual(square.size, 12)
        self.assertEqual(square.x, 44)
        self.assertEqual(square.y, 0)

    def test_three_valid_args(self):
        """..."""
        square = Square(15, 33, 88)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 33)
        self.assertEqual(square.y, 88)

    def test_size_init_string_size(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("45")

    def test_size_init_string_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(45, "11")

    def test_size_init_string_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(45, 11, "3")

    def test_size_init_negative_size(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-6)

    def test_size_init_negative_x(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(6, -7)

    def test_size_init_negative_y(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(6, 7, -8)

    def test_size_init_zero_size(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_square_str(self):
        """..."""
        sqr = Square(30, 15, 16, 222)
        sqr_str = "[Square] (222) 15/16 - 30"
        self.assertEqual(str(sqr), sqr_str)

    def test_getter(self):
        """..."""
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_setter(self):
        """..."""
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)

    def test_string(self):
        """..."""
        square = Square(3)
        with self.assertRaises(TypeError):
            square.size = "Hi"

    def test_negative(self):
        """..."""
        square = Square(6)
        with self.assertRaises(ValueError):
            square.size = -5

    def test_zero(self):
        """..."""
        square = Square(6)
        with self.assertRaises(ValueError):
            square.size = 0

    def test_decimal(self):
        """..."""
        square = Square(6)
        with self.assertRaises(TypeError):
            square.size = 1.5

    def test_tuple(self):
        """..."""
        square = Square(7)
        with self.assertRaises(TypeError):
            square.size = (2, 8)

    def test_empty(self):
        """..."""
        square = Square(7)
        with self.assertRaises(TypeError):
            square.size = ""

    def test_none(self):
        """..."""
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = None

    def test_list(self):
        """..."""
        square = Square(4)
        with self.assertRaises(TypeError):
            square.size = [4, 7]

    def test_dict(self):
        """..."""
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = {"hi": 5, "world": 8}

    def test_width(self):
        """..."""
        square = Square(5)
        square.size = 6
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)

    def test_to_dictionary(self):
        """..."""
        Base._Base__nb_objects = 0

        square = Square(10, 2, 1, 9)
        square_dict = square.to_dictionary()
        expected = {"id": 9, "x": 2, "size": 10, "y": 1}
        self.assertEqual(square_dict, expected)

        square = Square(1, 0, 0, 9)
        square_dict = square.to_dictionary()
        expected = {"id": 9, "x": 0, "size": 1, "y": 0}
        self.assertEqual(square_dict, expected)

        square.update(5, 5, 5, 5)
        square_dict = square.to_dictionary()
        expected = {"id": 5, "x": 5, "size": 5, "y": 5}
        self.assertEqual(square_dict, expected)


class TestSquareCreate(unittest.TestCase):
    """..."""

    def test_square_create_1_arg(self):
        """..."""
        sqr = Square.create(**{"id": 6})
        self.assertEqual(sqr.id, 6)

    def test_square_create_2_args(self):
        """..."""
        sqr = Square.create(**{"id": 6, "size": 7})
        self.assertEqual(sqr.id, 6)
        self.assertEqual(sqr.size, 7)

    def test_square_create_3_args(self):
        """..."""
        sqr = Square.create(**{"id": 6, "size": 7, "x": 8})
        self.assertEqual(sqr.id, 6)
        self.assertEqual(sqr.size, 7)
        self.assertEqual(sqr.x, 8)

    def test_square_create_4_args(self):
        """..."""
        sqr = Square.create(**{"id": 6, "size": 7, "x": 8, "y": 9})
        self.assertEqual(sqr.id, 6)
        self.assertEqual(sqr.size, 7)
        self.assertEqual(sqr.x, 8)
        self.assertEqual(sqr.y, 9)


class TestSquareSaveToFile(unittest.TestCase):
    """..."""

    def test_square_save_to_file_none(self):
        """..."""
        Square.save_to_file(None)
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 0)

    def test_square_save_to_file_empty_list(self):
        """..."""
        Square.save_to_file([])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 0)
        self.assertIsInstance(objs, list)

    def test_square_save_to_file_list(self):
        """..."""
        Square.save_to_file([Square(1, 2, 3, 4)])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Square)
        self.assertEqual(objs[0].id, 4)
        self.assertEqual(objs[0].x, 2)
        self.assertEqual(objs[0].y, 3)
        self.assertEqual(objs[0].size, 1)


class TestSquareLoadFromFile(unittest.TestCase):
    """..."""

    def setUp(self):
        """..."""
        if Path("Square.json").is_file():
            Path("Square.json").unlink()

    def test_square_load_from_file_no_file(self):
        """..."""
        self.assertFalse(Path("Square.json").is_file())
        self.assertEqual(Square.load_from_file(), [])

    def test_square_load_from_existing_file(self):
        """..."""
        Square.save_to_file([Square(1, 2, 3, 4)])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Square)
        self.assertEqual(objs[0].id, 4)
        self.assertEqual(objs[0].x, 2)
        self.assertEqual(objs[0].y, 3)
        self.assertEqual(objs[0].size, 1)


if __name__ == "__main__":
    unittest.main()
