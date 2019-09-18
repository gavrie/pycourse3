from point import Point

def test_distance():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance(p2) == 5
    assert p1.distance(p2) == p1 - p2

def test_equals():
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    assert p1 == p2

def test_dict():
    p1 = Point(3, 4)
    p2 = Point(3, 4)

    d = {p1: 'p1', p2: 'p2'}

    assert len(d) == 1
