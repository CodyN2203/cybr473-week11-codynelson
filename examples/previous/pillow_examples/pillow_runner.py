import os  # Python Standard Library: Operating System Methods
from datetime import datetime  # Python Standard Library: Date/time utilities

from examples.previous.pillow_examples.extracting_gps_data import (
    extract_exif_gps_and_basics,
    extract_lat_lon_from_gps_tags,
)

if __name__ == "__main__":
    """
    pyExif Main Entry Point
    """
    print("\nExtract EXIF Data from JPEG Files")
    print(f"Script Started: {str(datetime.now())}")
    print()

    TARGET_FILE_PATH = "../../../images/test.jpg"

    if not os.path.isfile(TARGET_FILE_PATH):
        raise SystemExit("File not found: " + TARGET_FILE_PATH)

    gps_tags, basic_exif = extract_exif_gps_and_basics(TARGET_FILE_PATH)

    # If there is no readable EXIF at all, both are None
    if gps_tags is None and basic_exif is None:
        raise SystemExit("No readable EXIF data found in: " + TARGET_FILE_PATH)

    timestamp = basic_exif.get("timestamp", "NA")
    camera_make = basic_exif.get("camera_make", "NA")
    camera_model = basic_exif.get("camera_model", "NA")

    print("Photo Details")
    print("-------------")
    print("TimeStamp:    ", timestamp)
    print("Camera Make:  ", camera_make)
    print("Camera Model: ", camera_model)

    coordinate_info = extract_lat_lon_from_gps_tags(gps_tags) if gps_tags else None

    print("\nGeo-Location Data")
    print("-----------------")

    latitude_decimal = None
    longitude_decimal = None

    if coordinate_info:
        latitude_decimal = coordinate_info.get("latitude_decimal")
        longitude_decimal = coordinate_info.get("longitude_decimal")

        if latitude_decimal is not None and longitude_decimal is not None:
            print("Latitude:  ", f"{latitude_decimal:2.6f}")
            # .6f formats the value as a fixed-point number with exactly 6 digits after the decimal
            # (the leading number sets only a minimum width).
            print("Longitude: ", f"{longitude_decimal:2.6f}")
        else:
            print("Could not retrieve Latitude and Longitude.")
    else:
        print("No GPS EXIF Data found.")
