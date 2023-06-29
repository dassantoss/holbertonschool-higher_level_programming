#!/usr/bin/python3
""" Unittest for rectangle class
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import path, remove
from unittest.mock import patch


class Test_args(unittest.TestCase):
    """ Class for unittest of arguments """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_nowidth(self):
        """ Test for no width """
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_noheight(self):
        """ Test for no height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_nox(self):
        """ Test for no x """
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.x, 0)

    def test_noy(self):
        """ Test for no y """
        r1 = Rectangle(1, 1, 1)
        self.assertEqual(r1.y, 0)

    def test_noid(self):
        """ Test for no id """
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.id, 1)

    def test_id(self):
        """ Test for id """
        r1 = Rectangle(1, 1, 1, 1, 85)
        self.assertEqual(r1.id, 85)

    def test_extraarg(self):
        """ Test for no extra arguments """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 1, 1, 1)


class Test_width(unittest.TestCase):
    """ Class for unittest of width """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_widthintpos(self):
        """ Positive Int for Width """
        r1 = Rectangle(5, 1)
        self.assertEqual(r1.width, 5)

    def test_widthintneg(self):
        """ Negative Int for Width """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-5, 1)

    def test_widthintzero(self):
        """ Zero Int for Width """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 1)

    def test_widthfloat(self):
        """ pos float for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1.0, 1)

    def test_widthfloatneg(self):
        """ neg float for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle(-1.0, 1)

    def test_widthNone(self):
        """ None for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 1)

    def test_widthStr(self):
        """ Str for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 1)

    def test_widthList(self):
        """ List for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle([1], 1)

    def test_widthTuple(self):
        """ Tuple for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle((1, ), 1)

    def test_widthSet(self):
        """ Set for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle({1}, 1)

    def test_widthprivate(self):
        """ Check private Width """
        r1 = Rectangle(5, 1)
        self.assertEqual(r1.width, 5)
        with self.assertRaises(AttributeError):
            r1.__width


class Test_height(unittest.TestCase):
    """ Class for unittest of height """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_heightintpos(self):
        """ Positive Int for height """
        r1 = Rectangle(1, 5)
        self.assertEqual(r1.height, 5)

    def test_heightintneg(self):
        """ Negative Int for height """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -5)

    def test_heightintzero(self):
        """ Zero Int for height """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)

    def test_heightfloat(self):
        """ pos float for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1.0)

    def test_heightfloatneg(self):
        """ neg float for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, -1.0)

    def test_heightNone(self):
        """ None for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, None)

    def test_heightStr(self):
        """ Str for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "1")

    def test_heightList(self):
        """ List for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, [1])

    def test_heightTuple(self):
        """ Tuple for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, (1, ))

    def test_heightSet(self):
        """ Set for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, {1})

    def test_heightprivate(self):
        """ Check private Width """
        r1 = Rectangle(1, 5)
        self.assertEqual(r1.height, 5)
        with self.assertRaises(AttributeError):
            r1.__height


class Test_x(unittest.TestCase):
    """ Class for unittest of x """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_xintpos(self):
        """ Positive Int for x """
        r1 = Rectangle(1, 1, 5)
        self.assertEqual(r1.x, 5)

    def test_xintneg(self):
        """ Negative Int for x """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, -5)

    def test_xintzero(self):
        """ Zero Int for x """
        r1 = Rectangle(1, 1, 0)
        self.assertEqual(r1.x, 0)

    def test_xfloat(self):
        """ pos float for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1.0)

    def test_xfloatneg(self):
        """ neg float for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, -1.0)

    def test_xNone(self):
        """ None for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, None)

    def test_xStr(self):
        """ Str for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, "1")

    def test_xList(self):
        """ List for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, [1])

    def test_xTuple(self):
        """ Tuple for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, (1, ))

    def test_xSet(self):
        """ Set for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, {1})

    def test_xprivate(self):
        """ Check private x """
        r1 = Rectangle(1, 1, 5)
        self.assertEqual(r1.x, 5)
        with self.assertRaises(AttributeError):
            r1.__x


class Test_y(unittest.TestCase):
    """ Class for unittest of y """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_yintpos(self):
        """ Positive Int for y """
        r1 = Rectangle(1, 1, 1, 5)
        self.assertEqual(r1.y, 5)

    def test_yintneg(self):
        """ Negative Int for y """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, 1, -5)

    def test_yintzero(self):
        """ Zero Int for y """
        r1 = Rectangle(1, 1, 1, 0)
        self.assertEqual(r1.y, 0)

    def test_yfloat(self):
        """ pos float for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 1.0)

    def test_yfloatneg(self):
        """ neg float for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, -1.0)

    def test_yNone(self):
        """ None for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, None)

    def test_yStr(self):
        """ Str for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, "1")

    def test_yList(self):
        """ List for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, [1])

    def test_yTuple(self):
        """ Tuple for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, (1, ))

    def test_ySet(self):
        """ Set for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, {1})

    def test_yprivate(self):
        """ Check private y """
        r1 = Rectangle(1, 1, 1, 5)
        self.assertEqual(r1.y, 5)
        with self.assertRaises(AttributeError):
            r1.__y


class Test_area(unittest.TestCase):
    """ Class for unittest of area method """

    def test_area1(self):
        """ Area 1 """
        r1 = Rectangle(2, 5)
        self.assertEqual(r1.area(), 10)

    def test_area2(self):
        """ Area 2 """
        r1 = Rectangle(1, 4)
        self.assertEqual(r1.area(), 4)

    def test_area3(self):
        """ Area 2 """
        r1 = Rectangle(3, 3, 1, 1, 1)
        self.assertEqual(r1.area(), 9)


class Test_display(unittest.TestCase):
    """ Class for unittest of display method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_noxy0(self):
        """ Display no XY """
        r1 = Rectangle(1, 1)
        dp = "#\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_noxy1(self):
        """ Display no XY """
        r1 = Rectangle(2, 2)
        dp = "##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_noxy2(self):
        """ Display no XY """
        r1 = Rectangle(3, 2)
        dp = "###\n###\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_noxy3(self):
        """ Display no XY """
        r1 = Rectangle(2, 3)
        dp = "##\n##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_noy0(self):
        """ Display no Y """
        r1 = Rectangle(2, 3, 1)
        dp = " ##\n ##\n ##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_noy1(self):
        """ Display no Y """
        r1 = Rectangle(2, 3, 1)
        r1.x = 3
        dp = "   ##\n   ##\n   ##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_xydisplay0(self):
        """ Display XY """
        r1 = Rectangle(2, 3, 1, 2)
        dp = "\n\n ##\n ##\n ##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_xydisplay1(self):
        """ Display XY """
        r1 = Rectangle(2, 3, 1, 2)
        r1.x = 2
        r1.y = 3
        dp = "\n\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)


class Test_str(unittest.TestCase):
    """ Class for unittest of __str__ method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_str1(self):
        """ Test for __str__ """
        r1 = Rectangle(2, 3)
        st = "[Rectangle] (1) 0/0 - 2/3"
        strP = str(r1)
        self.assertEqual(st, strP)
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(r1, end='')
            pr = p.getvalue()
        self.assertEqual(st, pr)

    def test_str2(self):
        """ Test for __str__ """
        r1 = Rectangle(2, 3, 5)
        st = "[Rectangle] (1) 5/0 - 2/3"
        strP = str(r1)
        self.assertEqual(st, strP)
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(r1, end='')
            pr = p.getvalue()
        self.assertEqual(st, pr)

    def test_str3(self):
        """ Test for __str__ """
        r1 = Rectangle(2, 3, 5, 6)
        st = "[Rectangle] (1) 5/6 - 2/3"
        strP = str(r1)
        self.assertEqual(st, strP)
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(r1, end='')
            pr = p.getvalue()
        self.assertEqual(st, pr)

    def test_str4(self):
        """ Test for __str__ """
        r1 = Rectangle(2, 3, 5, 6, 85)
        st = "[Rectangle] (85) 5/6 - 2/3"
        strP = str(r1)
        self.assertEqual(st, strP)
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(r1, end='')
            pr = p.getvalue()
        self.assertEqual(st, pr)

    def test_str5(self):
        """ Test for __str__ """
        r1 = Rectangle(2, 3, 5, 6, 85)
        r1.id = 9
        r1.x = 8
        r1.y = 7
        r1.width = 6
        r1.height = 5
        st = "[Rectangle] (9) 8/7 - 6/5"
        strP = str(r1)
        self.assertEqual(st, strP)
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(r1, end='')
            pr = p.getvalue()
        self.assertEqual(st, pr)


class Test_update(unittest.TestCase):
    """ Class for unittest of update method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_noargs(self):
        """ Did not Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update()
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 6)

    def test_upid(self):
        """ Id Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 85)

    def test_upwidth(self):
        """ Width Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85, 12)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 85)

    def test_upheight(self):
        """ Height Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85, 12, 8)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 85)

    def test_upx(self):
        """ X Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85, 12, 8, 0)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 85)

    def test_upy(self):
        """ Y Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85, 12, 8, 0, 7)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 7)
        self.assertEqual(r1.id, 85)

    def test_Kignore(self):
        """ Ignore Kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85, id=15, width=16, height=17, x=18, y=19)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 85)

    def test_Kid(self):
        """ id kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(id=15)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 15)

    def test_Kwidth(self):
        """ width kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(width=16, id=15)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 15)

    def test_Kheight(self):
        """ height kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(width=16, id=15, height=17)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 15)

    def test_Kx(self):
        """ x kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(x=18, width=16, id=15, height=17)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 18)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 15)

    def test_Ky(self):
        """ y kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(x=18, width=16, y=19, id=15, height=17)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 18)
        self.assertEqual(r1.y, 19)
        self.assertEqual(r1.id, 15)

    def test_Kfullchange(self):
        """ Full change kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(id=15, width=16, height=17, x=18, y=19)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 18)
        self.assertEqual(r1.y, 19)
        self.assertEqual(r1.id, 15)

    def test_Kfullchange2(self):
        """ Full change kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        d1 = {"id": 15, "width": 16, "height": 17, "x": 18, "y": 19}
        r1.update(**d1)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 18)
        self.assertEqual(r1.y, 19)
        self.assertEqual(r1.id, 15)


class Test_to_dictionary(unittest.TestCase):
    """ Class for unittest of to_dictionary method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_dic1(self):
        """ to dic test """
        r1 = Rectangle(2, 3)
        d1 = r1.to_dictionary()
        dic1 = {"width": 2, "height": 3, "x": 0, "y": 0, "id": 1}
        self.assertEqual(dic1["width"], d1["width"])
        self.assertEqual(dic1["height"], d1["height"])
        self.assertEqual(dic1["x"], d1["x"])
        self.assertEqual(dic1["y"], d1["y"])
        self.assertEqual(dic1["id"], d1["id"])

    def test_dic2(self):
        """ to dic test """
        r1 = Rectangle(3, 2, 4)
        d1 = r1.to_dictionary()
        dic1 = {"width": 3, "height": 2, "x": 4, "y": 0, "id": 1}
        self.assertEqual(dic1["width"], d1["width"])
        self.assertEqual(dic1["height"], d1["height"])
        self.assertEqual(dic1["x"], d1["x"])
        self.assertEqual(dic1["y"], d1["y"])
        self.assertEqual(dic1["id"], d1["id"])

    def test_dic3(self):
        """ to dic test """
        r1 = Rectangle(6, 1, 4, 5)
        d1 = r1.to_dictionary()
        dic1 = {"width": 6, "height": 1, "x": 4, "y": 5, "id": 1}
        self.assertEqual(dic1["width"], d1["width"])
        self.assertEqual(dic1["height"], d1["height"])
        self.assertEqual(dic1["x"], d1["x"])
        self.assertEqual(dic1["y"], d1["y"])
        self.assertEqual(dic1["id"], d1["id"])

    def test_dic4(self):
        """ to dic test """
        r1 = Rectangle(12, 13, 14, 15, 82)
        d1 = r1.to_dictionary()
        dic1 = {"width": 12, "height": 13, "x": 14, "y": 15, "id": 82}
        self.assertEqual(dic1["width"], d1["width"])
        self.assertEqual(dic1["height"], d1["height"])
        self.assertEqual(dic1["x"], d1["x"])
        self.assertEqual(dic1["y"], d1["y"])
        self.assertEqual(dic1["id"], d1["id"])

    def test_dic5(self):
        """ to dic test """
        r1 = Rectangle(12, 13, 14, 15, 82)
        d1 = r1.to_dictionary()
        dic1 = {"width": 12, "height": 13, "x": 14, "y": 15, "id": 82}
        self.assertEqual(dic1["width"], d1["width"])
        self.assertEqual(dic1["height"], d1["height"])
        self.assertEqual(dic1["x"], d1["x"])
        self.assertEqual(dic1["y"], d1["y"])
        self.assertEqual(dic1["id"], d1["id"])

        dic2 = {"width": 21, "height": 31, "x": 41, "y": 51, "id": 28}
        r1.update(**dic2)
        d2 = r1.to_dictionary()
        self.assertEqual(dic2["width"], d2["width"])
        self.assertEqual(dic2["height"], d2["height"])
        self.assertEqual(dic2["x"], d2["x"])
        self.assertEqual(dic2["y"], d2["y"])
        self.assertEqual(dic2["id"], d2["id"])
