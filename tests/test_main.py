
import os
import sys

import pytest
from reproj import reproj
from shapely.geometry import shape, Point, LineString, Polygon, MultiPolygon



# EXAMPLES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "examples")
# polygons = os.path.join(EXAMPLES, "polygons.shp")


@pytest.fixture
def example_point():
    # https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
    return Point(1, 2)


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



def test_main(example_point):
    reproj(example_point, 4326, 32630)


# def test_reproj_point(point):
#     assert reproj(example_point(), 4326, 32630) == ???


# def test_reproj_line(line):
#     assert reproj(line, 4326, 32630) == ???


# def test_reproj_polygon(polygon):
#     assert reproj(polygon, 4326, 32630) == ???


# def test_reproj_multipolygon(multipolygon):
#     assert reproj(multipolygon, 4326, 32630) == ???


# def test_bad_build_distance_array(example_raster_array):
#     with pytest.raises(TypeError):
#         reproj(???)

#     with pytest.raises(ValueError):
#         reproj(???)

#     with pytest.raises(Exception):
#         reproj(???)
