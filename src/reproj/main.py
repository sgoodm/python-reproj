import pyproj
import shapely.ops


def reproj(feat, src_crs, dst_crs):
    """Reproject a feature from one CRS to another.

    https://shapely.readthedocs.io/en/stable/manual.html?highlight=transform#shapely.ops.transform
    https://pyproj4.github.io/pyproj/stable/gotchas.html#upgrading-to-pyproj-2-from-pyproj-1


    Parameters
    ----------
    feat : shapely.geometry
        A feature to reproject.
    src_crs : int|str
        The source CRS. May be defined as int (e.g., 4326) or string (e.g., 'EPSG:4326')
    dst_crs : int|str
        The destination CRS. May be defined as int (e.g., 32630) or string (e.g., 'EPSG:32630')

    Returns
    -------
    shapely.geometry
        The reprojected feature.

    """

    new_transformer = pyproj.Transformer.from_crs(src_crs, dst_crs)

    reproj_feat = shapely.ops.transform(new_transformer.transform, feat)

    return reproj_feat
