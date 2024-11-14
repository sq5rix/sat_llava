from io import BytesIO

import ee
import requests
from PIL import Image

from llava import describe_picture


class Sat:
    """
    get sat image
    find and describe land features
    """

    def __init__(self):
        ee.Authenticate()
        ee.Initialize()


def get_and_export_image(self, x, y):
    # Define the EPSG:2180 projection (ETRS-LAEA)
    point = ee.Geometry.Point([x, y])
    laea_proj = ee.Projection("EPSG:2180")
    point_laea = ee.Geometry.Point([x, y], laea_proj)
    landsat = (
        ee.ImageCollection("LANDSAT/LC08/C01/T1_SR").filterBounds(point_laea).first()
    )
    thumb_url = landsat.getThumbUrl(
        {"min": 0, "max": 3000, "bands": ["B5", "B4", "B3"]}
    )
    response = requests.get(thumb_url)
    img = Image.open(BytesIO(response.content))
    img.save(f"images/{x}_{y}.png")


def main():
    sat = Sat()
    set.get_and_export_image(point)


if __name__ == "__main__":
    main()
