#!/usr/bin/python3
"""Unittests for Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """..."""

    def test_base_1_init_with_id(self):
        """..."""
        b = Base(123)
        self.assertEqual(b.id, 123)

    def test_base_2_init_without_id(self):
        """..."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_3_multiple_instances(self):
        """..."""
        b1 = Base()
        b2 = Base()
        b3 = Base(456)
        self.assertEqual(b1.id, 3)
        self.assertEqual(b2.id, 4)
        self.assertEqual(b3.id, 456)

    def test_base_4_to_json_string(self):
        """..."""
        self.assertEqual(Base.to_json_string([]), "[]")
        ld1 = Base.to_json_string([{'id': 21, 'name': 'json'}])
        self.assertEqual(ld1, '[{"id": 21, "name": "json"}]')
        ld2 = Base.to_json_string([{'id': 21, 'name': 'json'},
                                   {'age': 25, 'class': 4}])
        self.assertEqual(ld2, '[{"id": 21, "name": "json"}, '
                         '{"age": 25, "class": 4}]')
        self.assertIsInstance(ld2, str)

    def test_base_5_from_json_string(self):
        """..."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        ld1 = Base.from_json_string('[{"id": 21, "name": "json"}]')
        self.assertEqual(ld1, [{'id': 21, 'name': 'json'}])
        ld2 = Base.from_json_string('[{"id": 21, "name": "json"}, '
                                    '{"age": 25, "class": 4}]')
        self.assertEqual(ld2, [{'id': 21, 'name': 'json'},
                               {'age': 25, 'class': 4}])
        self.assertIsInstance(ld2, list)


if __name__ == '__main__':
    unittest.main()
