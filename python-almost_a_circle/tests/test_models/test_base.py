#!/usr/bin/python3
""" Unittest for base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import path, remove


class Test_id(unittest.TestCase):
    """ Class for unittest of __init__ and id """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_no_arg(self):
        """ Id no argument """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_none(self):
        """ Id None """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base(None)
        self.assertEqual(b3.id, 3)

    def test_ints(self):
        """ Id int """
        b1 = Base(5)
        self.assertEqual(b1.id, 5)
        b2 = Base(-5)
        self.assertEqual(b2.id, -5)
        b3 = Base()
        self.assertEqual(b3.id, 1)

    def test_extra_args(self):
        """ More than 1 argument """
        with self.assertRaises(TypeError):
            b1 = Base(5, 1)

    def test_private(self):
        """ Check priv attribute in instance """
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects


class Test_instance(unittest.TestCase):
    """ Clas for unittest of  instance """

    def test_base_self(self):
        """ Check if is instance """
        b1 = Base()
        self.assertTrue(isinstance(b1, Base))

    def test_Rectangle(self):
        """ Check if is instance """
        r1 = Rectangle(1, 1)
        self.assertTrue(isinstance(r1, Base))

    def test_Square(self):
        """ Check if is instance """
        s1 = Square(1)
        self.assertTrue(isinstance(s1, Base))


class Test_to_json_string(unittest.TestCase):
    """ Class for unittest of to_json_string method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_conversion(self):
        """ Conversion with None, empty list, and dicts"""

        l0 = None
        j0 = Base.to_json_string(l0)
        self.assertEqual(j0, "[]")
        self.assertEqual(type(j0), str)

        l1 = []
        j1 = Base.to_json_string(l1)
        self.assertEqual(j1, "[]")
        self.assertEqual(type(j1), str)

        l2 = [{}]
        j2 = Base.to_json_string(l2)
        self.assertEqual(j2, "[{}]")
        self.assertEqual(type(j2), str)

        l3 = [{'x': 1, 'y': 2}]
        j3 = Base.to_json_string(l3)
        st = str(l3)
        self.assertEqual(j3, st.replace("'", "\""))
        self.assertEqual(type(j3), str)

        l4 = [{'x': 1, 'y': 2}, {'a': 3, 'b': 4}]
        j4 = Base.to_json_string(l4)
        st = str(l4)
        self.assertEqual(j4, st.replace("'", "\""))
        self.assertEqual(type(j4), str)

    def test_Rectangle(self):
        """ Test with Rectangle instance """
        r1 = Rectangle(10, 7, 2, 8)
        l1 = [r1.to_dictionary()]
        j1 = Base.to_json_string(l1)
        st = str(l1)
        self.assertEqual(j1, st.replace("'", "\""))

    def test_Square(self):
        """ Test with Square instance """
        s1 = Square(10, 2, 8)
        l1 = [s1.to_dictionary()]
        j1 = Base.to_json_string(l1)
        st = str(l1)
        self.assertEqual(j1, st.replace("'", "\""))


class Test_from_json_string(unittest.TestCase):
    """ Class for unittest of from_json_string method """
    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_conversion(self):
        """ Conversion with None, empty list, and dicts"""

        l0 = None
        j0 = Base.to_json_string(l0)
        nl0 = Base.from_json_string(j0)
        self.assertEqual(nl0, [])
        self.assertEqual(type(j0), str)
        self.assertEqual(type(nl0), list)

        l1 = []
        j1 = Base.to_json_string(l1)
        nl1 = Base.from_json_string(j1)
        self.assertEqual(nl1, [])
        self.assertEqual(type(j1), str)
        self.assertEqual(type(nl1), list)

        l2 = [{}]
        j2 = Base.to_json_string(l2)
        nl2 = Base.from_json_string(j2)
        self.assertEqual(nl2, [{}])
        self.assertEqual(type(j2), str)
        self.assertEqual(type(nl2), list)

        l3 = [{'x': 1, 'y': 2}]
        j3 = Base.to_json_string(l3)
        nl3 = Base.from_json_string(j3)
        self.assertEqual(l3, nl3)
        self.assertEqual(type(j3), str)
        self.assertEqual(type(nl3), list)

        l4 = [{'x': 1, 'y': 2}, {'a': 3, 'b': 4}]
        j4 = Base.to_json_string(l4)
        nl4 = Base.from_json_string(j4)
        self.assertEqual(l4, nl4)
        self.assertEqual(type(j4), str)
        self.assertEqual(type(nl4), list)

    def test_Rectangle(self):
        """ Test with Rectangle instance """
        r1 = Rectangle(10, 7, 2, 8)
        l1 = [r1.to_dictionary()]
        j1 = Base.to_json_string(l1)
        nl1 = Base.from_json_string(j1)
        self.assertEqual(l1, nl1)
        self.assertEqual(type(j1), str)
        self.assertEqual(type(nl1), list)

    def test_Square(self):
        """ Test with Square instance """
        s1 = Square(10, 2, 8)
        l1 = [s1.to_dictionary()]
        j1 = Base.to_json_string(l1)
        nl1 = Base.from_json_string(j1)
        self.assertEqual(l1, nl1)
        self.assertEqual(type(j1), str)
        self.assertEqual(type(nl1), list)


class Test_create(unittest.TestCase):
    """ Class for unittest of create method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_Rectangle1(self):
        """ Test with different Rectangle instances """
        r1 = Rectangle(3, 5)
        d1 = r1.to_dictionary()
        r2 = Rectangle.create(**d1)
        st1 = str(r1)
        st2 = str(r2)
        self.assertEqual(st1, st2)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_Rectangle2(self):
        """ Test with different Rectangle instances """
        r1 = Rectangle(3, 5, 8)
        d1 = r1.to_dictionary()
        r2 = Rectangle.create(**d1)
        st1 = str(r1)
        st2 = str(r2)
        self.assertEqual(st1, st2)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_Rectangle3(self):
        """ Test with different Rectangle instances """
        r1 = Rectangle(3, 5, 8, 6)
        d1 = r1.to_dictionary()
        r2 = Rectangle.create(**d1)
        st1 = str(r1)
        st2 = str(r2)
        self.assertEqual(st1, st2)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_Rectangle4(self):
        """ Test with different Rectangle instances """
        r1 = Rectangle(3, 5, 8, 6, 85)
        d1 = r1.to_dictionary()
        r2 = Rectangle.create(**d1)
        st1 = str(r1)
        st2 = str(r2)
        self.assertEqual(st1, st2)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_Square1(self):
        """ Test with different Square instances """
        s1 = Square(3)
        d1 = s1.to_dictionary()
        s2 = Square.create(**d1)
        st1 = str(s1)
        st2 = str(s2)
        self.assertEqual(st1, st2)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_Square2(self):
        """ Test with different Square instances """
        s1 = Square(3, 4)
        d1 = s1.to_dictionary()
        s2 = Square.create(**d1)
        st1 = str(s1)
        st2 = str(s2)
        self.assertEqual(st1, st2)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_Square3(self):
        """ Test with different Square instances """
        s1 = Square(3, 4, 5)
        d1 = s1.to_dictionary()
        s2 = Square.create(**d1)
        st1 = str(s1)
        st2 = str(s2)
        self.assertEqual(st1, st2)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_Square4(self):
        """ Test with different Square instances """
        s1 = Square(3, 4, 5, 82)
        d1 = s1.to_dictionary()
        s2 = Square.create(**d1)
        st1 = str(s1)
        st2 = str(s2)
        self.assertEqual(st1, st2)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_nokwarg(self):
        """ Test with no kwarg """
        s1 = Square(3, 4, 5, 82)
        d1 = s1.to_dictionary()
        with self.assertRaises(TypeError):
            s2 = Square.create(d1)


class Test_save_to_file(unittest.TestCase):
    """ Class for unittest of save_to_file method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("Rectangle.json")
        except:
            pass
        try:
            remove("Square.json")
        except:
            pass

    def test_Nofile(self):
        """ Error when file does not exist """
        name = "Rectangle.json"
        with self.assertRaises(FileNotFoundError):
            with open(name, "r") as myfile:
                r = myfile.read()
                self.assertEqual(r, '[]')

    def test_None(self):
        """ Try to save None """
        name = "Rectangle.json"
        Rectangle.save_to_file(None)
        self.assertTrue(path.isfile(name))

    def test_checkEmptyList(self):
        """ Checks Contents """
        name = "Rectangle.json"
        Rectangle.save_to_file([])
        with open(name, "r") as myfile:
            r = myfile.read()
            self.assertEqual(r, '[]')

    def test_checkNoneRec(self):
        """ Checks Contents """
        name = "Rectangle.json"
        Rectangle.save_to_file(None)
        with open(name, "r") as myfile:
            r = myfile.read()
            self.assertEqual(r, '[]')

    def test_rectangle(self):
        """ Check if file is created with correct name """
        name = "Rectangle.json"
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(path.isfile(name))

    def test_rectangle_content(self):
        """ Check if file is created with correct content """
        name = "Rectangle.json"
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        dic1 = r1.to_dictionary()
        dic2 = r2.to_dictionary()
        dlist = str([dic1, dic2])
        with open(name, "r") as myfile:
            r = myfile.read()
            self.assertEqual(dlist.replace("'", "\""), r)

    def test_checkNoneSq(self):
        """ Checks Contents """
        name = "Square.json"
        Square.save_to_file(None)
        with open(name, "r") as myfile:
            r = myfile.read()
            self.assertEqual(r, '[]')

    def test_square(self):
        """ Check if file is created with correct name """
        name = "Square.json"
        r1 = Square(10, 7, 2)
        r2 = Square(2)
        Square.save_to_file([r1, r2])
        self.assertTrue(path.isfile(name))

    def test_square_content(self):
        """ Check if file is created with correct content """
        name = "Square.json"
        s1 = Square(10, 7, 2)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        dic1 = s1.to_dictionary()
        dic2 = s2.to_dictionary()
        dlist = str([dic1, dic2])
        with open(name, "r") as myfile:
            r = myfile.read()
            self.assertEqual(dlist.replace("'", "\""), r)

    def test_square_empty(self):
        """ Check if file is created with correct content empty """
        name = "Square.json"
        Square.save_to_file([])
        dlist = "[]"
        with open(name, "r") as myfile:
            r = myfile.read()
            self.assertEqual(dlist.replace("'", "\""), r)


class Test_load_from_file(unittest.TestCase):
    """ Class for unittest of load_from_file method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("Rectangle.json")
        except:
            pass
        try:
            remove("Square.json")
        except:
            pass

    def test_no_file(self):
        """ Test when file does not exist """
        rl1 = Rectangle.load_from_file()
        self.assertEqual(rl1, [])

    def test_empty_file_list(self):
        """ Test when file is empty list """
        Rectangle.save_to_file(None)
        rl1 = Rectangle.load_from_file()
        self.assertEqual(rl1, [])

    def test_rectangle_ins(self):
        """ Test for Rectangle instance """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        rl1 = Rectangle.load_from_file()
        self.assertTrue(isinstance(rl1[0], Rectangle))
        self.assertTrue(isinstance(rl1[1], Rectangle))

    def test_rectangle_data(self):
        """ Test for Rectangle instance data """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        rl1 = Rectangle.load_from_file()
        st1 = str(rl1[0])
        st2 = str(rl1[1])
        self.assertEqual(str(r1), st1)
        self.assertEqual(str(r2), st2)

    def test_square_ins(self):
        """ Test for Square instance """
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        sl1 = Square.load_from_file()
        self.assertTrue(isinstance(sl1[0], Square))
        self.assertTrue(isinstance(sl1[1], Square))

    def test_square_ins_data(self):
        """ Test for Square instance data """
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        sl1 = Square.load_from_file()
        st1 = str(sl1[0])
        st2 = str(sl1[1])
        self.assertEqual(str(s1), st1)
        self.assertEqual(str(s2), st2)


class Test_save_to_file_csv(unittest.TestCase):
    """ Class for unittest of save_to_file_csv method """
    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("Rectangle.csv")
        except:
            pass
        try:
            remove("Square.csv")
        except:
            pass

    def test_Nofile_csv(self):
        """ Error when file does not exist """
        name = "Rectangle.csv"
        with self.assertRaises(FileNotFoundError):
            with open(name, "r") as myfile:
                r = myfile.read()
                self.assertEqual(r, '[]')

    def test_None_csv(self):
        """ Try to save None """
        name = "Rectangle.csv"
        Rectangle.save_to_file_csv(None)
        self.assertTrue(path.isfile(name))

    def test_checkEmptyList_csv(self):
        """ Checks Contents """
        name = "Rectangle.csv"
        Rectangle.save_to_file_csv([])
        with open(name, "r") as myfile:
            r = myfile.read()
            self.assertEqual(r, '')

    def test_checkNoneRec_csv(self):
        """ Checks Contents """
        name = "Rectangle.csv"
        Rectangle.save_to_file_csv(None)
        with open(name, "r") as myfile:
            r = myfile.read()
            self.assertEqual(r, '')

    def test_rectangle_csv(self):
        """ Check if file is created with correct name """
        name = "Rectangle.csv"
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        self.assertTrue(path.isfile(name))

    def test_rectangle_content(self):
        """ Check if file is created with correct content """
        name = "Rectangle.csv"
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        nl = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(nl[0]))
        self.assertEqual(str(r2), str(nl[1]))

    def test_checkNoneSq_csv(self):
        """ Checks Contents """
        name = "Square.csv"
        Square.save_to_file_csv(None)
        with open(name, "r") as myfile:
            r = myfile.read()
            self.assertEqual(r, '')

    def test_square_csv(self):
        """ Check if file is created with correct name """
        name = "Square.csv"
        s1 = Square(10, 7, 2)
        s2 = Square(2)
        Square.save_to_file_csv([s1, s2])
        self.assertTrue(path.isfile(name))

    def test_square_content_csv(self):
        """ Check if file is created with correct content """
        name = "Square.csv"
        s1 = Square(10, 7, 2)
        s2 = Square(2)
        Square.save_to_file_csv([s1, s2])
        nl = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(nl[0]))
        self.assertEqual(str(s2), str(nl[1]))


class Test_load_from_file_csv(unittest.TestCase):
    """ Class for unittest of load_from_file_csv method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("Rectangle.csv")
        except:
            pass
        try:
            remove("Square.csv")
        except:
            pass

    def test_no_file_csv(self):
        """ Test when file does not exist """
        rl1 = Rectangle.load_from_file_csv()
        self.assertEqual(rl1, [])

    def test_empty_file_list_csv(self):
        """ Test when file is empty list """
        Rectangle.save_to_file_csv(None)
        rl1 = Rectangle.load_from_file_csv()
        self.assertEqual(rl1, [])

    def test_rectangle_ins_csv(self):
        """ Test for Rectangle instance """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        rl1 = Rectangle.load_from_file_csv()
        self.assertTrue(isinstance(rl1[0], Rectangle))
        self.assertTrue(isinstance(rl1[1], Rectangle))

    def test_rectangle_data_csv(self):
        """ Test for Rectangle instance data """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        rl1 = Rectangle.load_from_file_csv()
        st1 = str(rl1[0])
        st2 = str(rl1[1])
        self.assertEqual(str(r1), st1)
        self.assertEqual(str(r2), st2)

    def test_square_ins_csv(self):
        """ Test for Square instance """
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        sl1 = Square.load_from_file_csv()
        self.assertTrue(isinstance(sl1[0], Square))
        self.assertTrue(isinstance(sl1[1], Square))

    def test_square_ins_data_csv(self):
        """ Test for Square instance data """
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        sl1 = Square.load_from_file_csv()
        st1 = str(sl1[0])
        st2 = str(sl1[1])
        self.assertEqual(str(s1), st1)
        self.assertEqual(str(s2), st2)
