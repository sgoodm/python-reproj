
import pytest
from reproj import reproj
from shapely.geometry import shape, Point, LineString, Polygon, MultiPolygon
from pyproj.exceptions import CRSError
import fiona


@pytest.fixture
def example_point_a():
    # https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
    return Point(-1, 6)


@pytest.fixture
def example_point_b():
    # https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
    return Point(0, 6)


@pytest.fixture
def example_shape():
    return shape({"type": "Point", "coordinates": [-1, 6]})


def test_reproj_point(example_point_a, example_point_b):

    reproj_a = reproj(example_point_a, 4326, 32630)
    assert round(reproj_a.x, 3) == 721383.146
    assert round(reproj_a.y, 3) == 663608.575

    reproj_b = reproj(example_point_b, 4326, 32631)
    assert round(reproj_b.x, 3) == 167842.208
    assert round(reproj_b.y, 3) == 664114.162


def test_reproj_point(example_shape):

    reproj_a = reproj(example_shape, 4326, 32630)
    assert round(reproj_a.x, 3) == 721383.146
    assert round(reproj_a.y, 3) == 663608.575


def test_reproj_line():
    src_4326 = fiona.open('./examples/data/linestring_4326.geojson')
    src_32630 = fiona.open('./examples/data/linestring_32630.geojson')
    assert round(reproj(shape(src_4326[0].geometry), 4326, 32630).length, 3) == round(shape(src_32630[0].geometry).length, 3)


def test_reproj_polygon():
    src_4326 = fiona.open('./examples/data/polygon_4326.geojson')
    src_32630 = fiona.open('./examples/data/polygon_32630.geojson')
    assert round(reproj(shape(src_4326[0].geometry), 4326, 32630).area, 3) == round(shape(src_32630[0].geometry).area, 3)


def test_reproj_multipolygon():
    src_4326 = fiona.open('./examples/data/multipolygon_4326.geojson')
    src_32630 = fiona.open('./examples/data/multipolygon_32630.geojson')
    assert round(reproj(shape(src_4326[0].geometry), 4326, 32630).area, 3) == round(shape(src_32630[0].geometry).area, 3)


def test_valid_crs():
    reproj(Point(1,1), 4326, 32630)
    reproj(Point(1,1), 4326, 'EPSG:32630')
    reproj(Point(1,1), 4326, 'epsg:32630')


def test_invalid_crs():

    # with pytest.raises(CRSError):
    #     reproj(Point(1,1), 4326, '32630')

    with pytest.raises(CRSError):
        reproj(Point(1,1), 4326, 123456789)

    with pytest.raises(CRSError):
        reproj(Point(1,1), 4326, 'abc123')
