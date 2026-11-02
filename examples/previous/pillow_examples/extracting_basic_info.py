import os  # Python Standard Library: Operating System Methods
from datetime import datetime  # Python Standard Library: Date/time utilities
from PIL import Image

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

    try:
        with Image.open(TARGET_FILE_PATH) as image:
            exif_data = image.info
            height = image.height
            print(f"\n Height: {height}")
            print(f"\n Filename: {image.filename}")
            split_directory = image.filename.split('/')
            print(f"\n Extension: .{split_directory[-1].split('.')[1]}")
    except (OSError, ValueError):
        raise SystemExit("There was an issue with " + TARGET_FILE_PATH)


