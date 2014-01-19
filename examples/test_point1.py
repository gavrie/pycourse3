import pytest
from point1 import Point

def test_point_default():
    p = Point()
    assert p.x == 0
    assert p.y == 0

def test_point():
    p = Point(3, 4)
    assert p.x == 3
    assert p.y == 4

def test_point_equals():
    p1 = Point(3, 4)
    p2 = Point(3, 4)

    assert p1 == p2

def test_point_not_equals():
    p1 = Point(3, 4)
    p2 = Point(4, 5)

    assert p1 != p2

def test_point_in_dict():
    p1 = Point(3, 4)
    p2 = Point(4, 5)

    point_names = {}
    point_names[p1] = "First point"
    point_names[p2] = "Second point"

    assert point_names[p1] == "First point"
    assert point_names[p2] == "Second point"

def test_point_in_dict_with_same_hash():
    p1 = Point(3, 4)
    p2 = Point(3, 4)

    point_names = {}
    point_names[p1] = "First point"
    point_names[p2] = "Second point"

    assert len(point_names) == 1
    assert point_names[p2] == "Second point"

def test_hash():
    p1 = Point(4, 5)
    p2 = Point(4, 5)
    p3 = Point(2, 3)

    assert hash(p1) != hash(p3)
    assert hash(p1) == hash(p2)

def test_property():
    p1 = Point(4, 5)
    assert p1.x == 4

    with pytest.raises(AttributeError):
        p1.x = 5
