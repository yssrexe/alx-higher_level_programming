#!/usr/bin/python3
"""Unittests for testing Rectangle class"""
import io
import sys
import unittest
from pathlib import Path
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """..."""

    def setUp(self):
        """..."""
        self.rect = Rectangle(5, 7, 7, 5, 1)

    def test_inherits_base(self):
        """..."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """..."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """..."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """..."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """..."""
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """..."""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """..."""
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_over_five_args(self):
        """..."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_width_attribute(self):
        """..."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_private_height_attribute(self):
        """..."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_private_x_attribute(self):
        """..."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_private_y_attribute(self):
        """..."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """..."""
        self.assertEqual(5, self.rect.width)

    def test_width_setter(self):
        """..."""
        self.rect.width = 10
        self.assertEqual(10, self.rect.width)

    def test_height_getter(self):
        """..."""
        self.assertEqual(7, self.rect.height)

    def test_height_setter(self):
        """..."""
        self.rect.height = 10
        self.assertEqual(10, self.rect.height)

    def test_x_getter(self):
        """..."""
        self.assertEqual(7, self.rect.x)

    def test_x_setter(self):
        """..."""
        self.rect.x = 10
        self.assertEqual(10, self.rect.x)

    def test_y_getter(self):
        """..."""
        self.assertEqual(5, self.rect.y)

    def test_y_setter(self):
        """..."""
        self.rect.y = 10
        self.assertEqual(10, self.rect.y)


class TestRectangleWidth(unittest.TestCase):

    def test_none_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_list_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 2)

    def test_range_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b"Python", 2)

    def test_bytearray_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b"abcdefg"), 2)

    def test_memoryview_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b"abcedfg"), 2)

    def test_inf_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("inf"), 2)

    def test_nan_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("nan"), 2)

    def test_negative_width(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangleHeight(unittest.TestCase):
    """..."""

    def test_none_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3}))

    def test_range_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_bytes_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b"Python")

    def test_bytearray_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b"abcdefg"))

    def test_memoryview_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b"abcedfg"))

    def test_inf_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("inf"))

    def test_nan_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("nan"))

    def test_negative_height(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangleX(unittest.TestCase):
    """..."""

    def test_none_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_list_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3}))

    def test_range_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b"Python")

    def test_bytearray_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b"abcdefg"))

    def test_memoryview_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b"abcedfg"))

    def test_inf_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float("inf"), 2)

    def test_nan_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float("nan"), 2)

    def test_negative_x(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangleY(unittest.TestCase):
    """..."""

    def test_none_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3}))

    def test_range_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b"Python")

    def test_bytearray_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b"abcdefg"))

    def test_memoryview_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b"abcedfg"))

    def test_inf_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float("inf"))

    def test_nan_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float("nan"))

    def test_negative_y(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangeInvalidArgType(unittest.TestCase):
    """..."""

    def test_width_before_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", "height")

    def test_width_before_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 2, "x")

    def test_width_before_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 2, 3, "y")

    def test_height_before_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "height", "x")

    def test_height_before_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "height", 2, "y")

    def test_x_before_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "x", "y")


class TestRectangleArea(unittest.TestCase):
    """..."""

    def test_area_small(self):
        """..."""
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_one_arg(self):
        """..."""
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_area_large(self):
        """..."""
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_changed_attributes(self):
        """..."""
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())


class TestRectangleSTDOUT(unittest.TestCase):
    """..."""

    @staticmethod
    def read_stdout(rect, method):
        """..."""

        extr = io.StringIO()
        sys.stdout = extr
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return extr

    # Test __str__ method
    def test_str_method_print_width_height(self):
        """..."""
        r = Rectangle(4, 6)
        capture = TestRectangleSTDOUT.read_stdout(r, "print")
        correct = f"[Rectangle] ({r.id}) 0/0 - 4/6\n"
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        """..."""
        r = Rectangle(5, 5, 1)
        correct = f"[Rectangle] ({r.id}) 1/0 - 5/5"
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        """..."""
        r = Rectangle(1, 8, 2, 4)
        correct = f"[Rectangle] ({r.id}) 2/4 - 1/8"
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        """..."""
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        """..."""
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        """..."""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
    def test_display_width_height(self):
        """..."""
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangleSTDOUT.read_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        """..."""
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangleSTDOUT.read_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        """..."""
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangleSTDOUT.read_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        """..."""
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangleSTDOUT.read_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        """..."""
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangleUpdateArgs(unittest.TestCase):
    """..."""

    def setUp(self):
        """..."""
        self.rectangle = Rectangle(10, 10, 10, 10, 10)

    def test_update_args_zero(self):
        """..."""
        self.rectangle.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(self.rectangle))

    def test_update_args_one(self):
        """..."""
        self.rectangle.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(self.rectangle))

    def test_update_args_two(self):
        """..."""
        self.rectangle.update(89)
        self.rectangle.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(self.rectangle))

    def test_update_args_three(self):
        """..."""
        self.rectangle.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(self.rectangle))

    def test_update_args_four(self):
        """..."""
        self.rectangle.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(self.rectangle))

    def test_update_args_five(self):
        """..."""
        self.rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(self.rectangle))

    def test_update_args_none_id(self):
        """..."""
        self.rectangle.update(None)
        correct = f"[Rectangle] ({self.rectangle.id}) 10/10 - 10/10"
        self.assertEqual(correct, str(self.rectangle))

    def test_update_args_none_id_and_more(self):
        """..."""
        self.rectangle.update(None, 4, 5, 2)
        correct = f"[Rectangle] ({self.rectangle.id}) 2/10 - 4/5"
        self.assertEqual(correct, str(self.rectangle))

    def test_update_args_twice(self):
        """..."""
        self.rectangle.update(89, 2, 3, 4, 5, 6)
        self.rectangle.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(self.rectangle))

    def test_update_args_invalid_width_type(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(89, "invalid")

    def test_update_args_width_zero(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.rectangle.update(89, 0)

    def test_update_args_width_negative(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.rectangle.update(89, -5)

    def test_update_args_invalid_height_type(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.rectangle.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.rectangle.update(89, 1, 0)

    def test_update_args_height_negative(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.rectangle.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.rectangle.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.rectangle.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.rectangle.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.rectangle.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.rectangle.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.rectangle.update(89, 1, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.rectangle.update(89, 1, 2, "invalid", "invalid")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """..."""

    def setUp(self):
        """..."""
        self.rectangle = Rectangle(10, 10, 10, 10, 10)

    def test_update_kwargs_one(self):
        """..."""
        self.rectangle.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(self.rectangle))

    def test_update_kwargs_two(self):
        """..."""
        self.rectangle.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(self.rectangle))

    def test_update_kwargs_three(self):
        """..."""
        self.rectangle.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(self.rectangle))

    def test_update_kwargs_four(self):
        """..."""
        self.rectangle.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(self.rectangle))

    def test_update_kwargs_five(self):
        """..."""
        self.rectangle.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(self.rectangle))

    def test_update_kwargs_none_id(self):
        """..."""
        self.rectangle.update(id=None)
        correct = f"[Rectangle] ({self.rectangle.id}) 10/10 - 10/10"
        self.assertEqual(correct, str(self.rectangle))

    def test_update_kwargs_none_id_and_more(self):
        """..."""
        self.rectangle.update(id=None, height=7, y=9)
        correct = f"[Rectangle] ({self.rectangle.id}) 10/9 - 10/7"
        self.assertEqual(correct, str(self.rectangle))

    def test_update_kwargs_twice(self):
        """..."""
        self.rectangle.update(id=89, x=1, height=2)
        self.rectangle.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(self.rectangle))

    def test_update_kwargs_invalid_width_type(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.rectangle.update(width=0)

    def test_update_kwargs_width_negative(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.rectangle.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.rectangle.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.rectangle.update(height=0)

    def test_update_kwargs_height_negative(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.rectangle.update(height=-5)

    def test_update_kwargs_invalid_x_type(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.rectangle.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.rectangle.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.rectangle.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.rectangle.update(y=-5)

    def test_update_args_and_kwargs(self):
        """..."""
        self.rectangle.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(self.rectangle))

    def test_update_kwargs_wrong_keys(self):
        """..."""
        self.rectangle.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(self.rectangle))

    def test_update_kwargs_some_wrong_keys(self):
        """..."""
        self.rectangle.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(self.rectangle))


class TestRectangleToDictionary(unittest.TestCase):
    """..."""

    def setUp(self):
        """..."""
        self.rect = Rectangle(10, 2, 1, 9, 5)

    def test_to_dictionary_output(self):
        """..."""
        expected_output = {"x": 1, "y": 9, "id": 5, "height": 2, "width": 10}
        self.assertDictEqual(expected_output, self.rect.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """..."""
        rect_a = Rectangle(5, 9, 1, 2, 10)
        rect_a.update(**self.rect.to_dictionary())
        self.assertNotEqual(self.rect, rect_a)

    def test_to_dictionary_with_argument(self):
        """..."""
        with self.assertRaises(TypeError):
            self.rect.to_dictionary(1)


class TestRectangleCreate(unittest.TestCase):
    """..."""

    def test_rectangle_create_1_arg(self):
        """..."""
        rect = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertIsInstance(rect, Rectangle)

    def test_rectangle_create_2_args(self):
        """..."""
        rect = Rectangle.create(**{'id': 76, 'width': 112})
        self.assertEqual(rect.id, 76)
        self.assertEqual(rect.width, 112)

    def test_rectangle_create_3_args(self):
        """..."""
        rect = Rectangle.create(**{'id': 24, 'width': 25, 'height': 11})
        self.assertEqual(rect.id, 24)
        self.assertEqual(rect.width, 25)
        self.assertEqual(rect.height, 11)

    def test_rectangle_create_4_args(self):
        """..."""
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_create_5_args(self):
        """..."""
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3,
                                   'y': 4})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)


class RectangleSaveToFile(unittest.TestCase):
    """..."""

    def test_rectangle_save_to_file_none(self):
        """..."""
        Rectangle.save_to_file(None)
        self.assertTrue(Path("Rectangle.json").is_file())
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 0)

    def test_rectangle_save_to_file_empty_list(self):
        """..."""
        Rectangle.save_to_file([])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 0)
        self.assertIsInstance(objs, list)

    def test_rectangle_save_to_file_list(self):
        """..."""
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Rectangle)
        self.assertEqual(objs[0].id, 5)
        self.assertEqual(objs[0].width, 1)
        self.assertEqual(objs[0].height, 2)
        self.assertEqual(objs[0].x, 3)
        self.assertEqual(objs[0].y, 4)


class TestRectangleLoadFromFile(unittest.TestCase):
    """..."""

    def setUp(self):
        """..."""
        if Path("Rectangle.json").is_file():
            Path("Rectangle.json").unlink()

    def test_rectangle_load_from_file_no_file(self):
        """..."""
        self.assertFalse(Path("Rectangle.json").is_file())
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangle_load_from_existing_file(self):
        """..."""
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Rectangle)
        self.assertEqual(objs[0].id, 5)
        self.assertEqual(objs[0].width, 1)
        self.assertEqual(objs[0].height, 2)
        self.assertEqual(objs[0].x, 3)
        self.assertEqual(objs[0].y, 4)


if __name__ == "__main__":
    unittest.main()
