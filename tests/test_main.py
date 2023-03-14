
import pytest
from reproj import reproj
from shapely.geometry import shape, Point, LineString, Polygon, MultiPolygon
from pyproj.exceptions import CRSError

@pytest.fixture
def example_point_a():
    # https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
    return Point(-1, 6)

@pytest.fixture
def example_point_b():
    # https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
    return Point(0, 6)

@pytest.fixture
def example_line():
    # https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
    return LineString([(1, 2), (1, 3), (2, 3)])

@pytest.fixture
def example_polygon():
    return Polygon([(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)])

@pytest.fixture
def example_multipolygon():
    return MultiPolygon([[(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)],
                         [(3, 3), (3, 4), (4, 4), (4, 3), (3, 3)]])

@pytest.fixture
def example_shape():
    return shape({"type": "Point", "coordinates": [1, 2]})


def test_reproj_point(example_point_a, example_point_b):

    reproj_a = reproj(example_point_a, 4326, 32630)
    assert round(reproj_a.x, 3) == 721383.146
    assert round(reproj_a.y, 3) == 663608.575

    reproj_b = reproj(example_point_b, 4326, 32631)
    assert round(reproj_b.x, 3) == 167842.208
    assert round(reproj_b.y, 3) == 664114.162


# def test_reproj_line(line):
#     assert reproj(line, 4326, 32630) == ???


# def test_reproj_polygon(polygon):
#     assert reproj(polygon, 4326, 32630) == ???


# def test_reproj_multipolygon(multipolygon):
#     assert reproj(multipolygon, 4326, 32630) == ???


def test_valid_crs():
    reproj(Point(1,1), 4326, 32630)
    reproj(Point(1,1), 4326, 'EPSG:32630')
    reproj(Point(1,1), 4326, 'epsg:32630')


def test_invalid_crs():

    with pytest.raises(CRSError):
        reproj(Point(1,1), 4326, '32630')

    with pytest.raises(CRSError):
        reproj(Point(1,1), 4326, 123456789)
