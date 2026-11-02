from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_exif_data(file_name):
    try:
        pil_image = Image.open(file_name)
        exif_data = pil_image.info
        return pil_image, exif_data
    except Exception:
        # If exception occurs from PIL processing
        print("Failed to extract EXIF data from " + file_name)
        return None, None

if __name__ == '__main__':
    DEBUG = False
    if DEBUG:
        print("Debug Mode is on, Showing more print statements")
    pil_image, exif_data = extract_exif_data('../images/test.jpg')

    if DEBUG:
        print(f"Exif Data is a : {type(exif_data)}")
    # Dictionary - So Let's See What Is In It
    for key, value in exif_data.items():
        if DEBUG:
            print(f"{key} : {value}\n")

    # Likely a bunch of numbers.
    # So we use the TAGS to make sense of it

    # Decode numeric tags using PIL TAGS
    print("\n--- Decoded EXIF Data ---")
    decoded_exif = {}

    for tag_id, value in exif_data.items():
        tag_name = TAGS.get(tag_id, tag_id)
        decoded_exif[tag_name] = value
        print(f"{tag_name} : {value}\n")
        # Note GPS Data Needs Additional Extracting



