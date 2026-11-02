from __future__ import annotations

from typing import Any, Dict, Optional, Tuple

from PIL import Image, ExifTags
from PIL.ExifTags import GPSTAGS


def extract_lat_lon_from_gps_tags(gps_tags: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Extract latitude/longitude from a GPS EXIF tag dictionary (already translated to GPSTAGS names).

    Expected GPS keys (common EXIF names):
        - "GPSLatitude"      : ((deg_num, deg_den), (min_num, min_den), (sec_num, sec_den))
        - "GPSLatitudeRef"   : "N" or "S"
        - "GPSLongitude"     : ((deg_num, deg_den), (min_num, min_den), (sec_num, sec_den))
        - "GPSLongitudeRef"  : "E" or "W"

    Returns:
        A dictionary with decimal coordinates and the original references, e.g.:
        {
            "latitude_decimal": 31.7619,
            "longitude_decimal": -106.4850,
            "latitude_ref": "N",
            "longitude_ref": "W",
        }

        Returns None if any required GPS fields are missing or malformed.
    """
    required_keys = ("GPSLatitude", "GPSLatitudeRef", "GPSLongitude", "GPSLongitudeRef")
    if not all(key in gps_tags for key in required_keys):
        return None

    try:
        latitude_dms = gps_tags["GPSLatitude"]
        latitude_ref = gps_tags["GPSLatitudeRef"]
        longitude_dms = gps_tags["GPSLongitude"]
        longitude_ref = gps_tags["GPSLongitudeRef"]

        latitude_decimal, longitude_decimal = convert_gps_dms_to_decimal(
            lat_dms=latitude_dms,
            lat_ref=latitude_ref,
            lon_dms=longitude_dms,
            lon_ref=longitude_ref,
        )

        return {
            "latitude_decimal": latitude_decimal,
            "longitude_decimal": longitude_decimal,
            "latitude_ref": latitude_ref,
            "longitude_ref": longitude_ref,
        }

    except (KeyError, TypeError, IndexError, ZeroDivisionError, ValueError) as e:
        print(f"OH NO! WE HAVE AN ERROR: {e}")
        return None


def extract_exif_gps_and_basics(image_path: str) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, str]]]:
    """
    Read an image file and extract:
      1) GPS metadata (decoded to human-readable GPSTAGS keys)
      2) A few basic EXIF fields useful in investigations

    Returns:
        (gps_tags, basic_exif)

        gps_tags: dict of GPS tags (empty dict if EXIF exists but no GPSInfo)
        basic_exif: dict with:
            - "timestamp"   (DateTimeOriginal)
            - "camera_make" (Make)
            - "camera_model"(Model)

        Returns (None, None) if the image cannot be opened OR has no readable EXIF.
    """
    try:
        with Image.open(image_path) as image:
            exif_data = image.getexif()
            # print(exif_data)
    except (OSError, ValueError):
        return None, None

    if not exif_data:
        return None, None

    basic_exif: Dict[str, str] = {
        "timestamp": "NA",
        "camera_make": "NA",
        "camera_model": "NA",
    }

    camera_make = exif_data.get(ExifTags.Base.Make)
    if camera_make:
        basic_exif['camera_make'] = camera_make.strip()

    camera_model = exif_data.get(ExifTags.Base.Model)
    if camera_model:
        basic_exif['camera_model'] = camera_model.strip()

    timestamp = exif_data.get(ExifTags.Base.DateTimeOriginal)
    if timestamp:
        basic_exif['timestamp'] = timestamp.strip()

    exif_ifd = exif_data.get_ifd(ExifTags.IFD.Exif)
    timestamp = exif_ifd.get(ExifTags.Base.DateTimeOriginal)
    if timestamp:
        basic_exif['timestamp'] = timestamp.strip()

    gps_ifd = exif_data.get_ifd(ExifTags.IFD.GPSInfo)
    # print(gps_ifd)

    gps_tags: Dict[str, Any] = {}

    for gps_id, gps_value in gps_ifd.items():
        gps_tag_name = GPSTAGS.get(gps_id, gps_id)
        gps_tags[gps_tag_name] = gps_value

    return gps_tags, basic_exif



def rational_to_float(rational: Any) -> float:
    """
    Convert an EXIF rational value into a float.

    EXIF stores many numbers as "Rational" values, typically:
        - (numerator, denominator) tuples, e.g. (30, 1)
        - Some photos have fractions like 5/0 (5 divided by 0),
          we cannot divide by zero so we return the numerator.
    Returns:
        float version of the value.
    """
    # Extract numerator and denominator

    if isinstance(rational, tuple):
        numerator, denominator = rational
    else:
        numerator = rational.numerator
        denominator = rational.denominator

    # Handle zero denominator
    if denominator == 0:
        return float(numerator)

    # Normal division
    return float(numerator) / float(denominator)

def convert_gps_dms_to_decimal(
    lat_dms: Any,
    lat_ref: str,
    lon_dms: Any,
    lon_ref: str,
) -> Tuple[float, float]:
    """
    Convert EXIF GPS coordinates from Degrees/Minutes/Seconds to decimal degrees.

    Degree Minute Second (DMS) format expected:
        lat_dms or lon_dms = (deg, min, sec)
        where each of deg/min/sec is usually a rational tuple: (num, den)

    Refs:
        lat_ref: "N" or "S"
        lon_ref: "E" or "W"

    Returns:
        (latitude_decimal, longitude_decimal)
    """

    lat_deg = rational_to_float(lat_dms[0])
    lat_min = rational_to_float(lat_dms[1])
    lat_sec = rational_to_float(lat_dms[2])

    latitude_decimal = lat_deg + (lat_min / 60.0) + (lat_sec / 3600.0)
    if lat_ref.upper() == "S":
        latitude_decimal *= -1.0

    lon_deg = rational_to_float(lon_dms[0])
    lon_min = rational_to_float(lon_dms[1])
    lon_sec = rational_to_float(lon_dms[2])

    longitude_decimal = lon_deg + (lon_min / 60.0) + (lon_sec / 3600.0)
    if lon_ref.upper() == "W":
        longitude_decimal *= -1.0

    return latitude_decimal, longitude_decimal

if __name__ == "__main__":
    extract_exif_gps_and_basics("../images/test.jpg")