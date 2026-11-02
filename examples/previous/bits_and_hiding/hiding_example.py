from PIL import Image  # pip install pillow
from least_significant_bits import extract_last_n_bits, replace_last_n_bits # From our other example

# Tiny Utility Functions

# Convert Ints from 0 to 255 to an 8-bit '0/1' string
def to_bits8(value: int) -> str:
    return format(value, '08b')

#  Convert an 8-bit string back to and int of 0 to 255
def from_bits8(bits8: str) -> int:
    if len(bits8) != 8 or any(b not in '01' for b in bits8):
        raise ValueError("bits8 must be exactly 8 characters of '0' or '1'")
    return int(bits8, 2)

# Pixels are made of 3 Colors - RGB
# Each Pixel from Pillow in a column or row has a value of red green or blue
# The red value is at index 0 Green at index 1 etc...
# We are creating constants here to easily access the pixel data here and make the code more readible.
RED = 0
GREEN = 1
BLUE = 2

try:
    # open our monalisa
    with Image.open("../../../assets/monalisa.bmp") as im:
        im = im.convert("RGB")
        picture = im.load() # load the image

        # Choose a pixel row/column to start with.
        column, row  = 0, 0
        width, height = im.size

        # We make sure this row column is in the image.
        if not (0 <= column < width and 0 <= row < height):
            raise ValueError("Row/Col out of bounds")

        # Read original pixel channels
        print(picture[column, row])
        original_red_value, original_green_value, original_blue_value = picture[column, row] # grab pixel using pix
        print("\nOriginal Pixel - Binary values:")
        print("RED:",  to_bits8(original_red_value))
        print("GREEN:",  to_bits8(original_green_value))
        print("BLUE:",  to_bits8(original_blue_value))

        # Example targets:
        # - set RED's last 1 bit to '1'
        # - set GREEN's last 1 bit to '0'
        # - set BLUE's last 2 bits to '10'

        # this can be done in a loop but for our purposes lets quickly hide these 6 bits

        hide_me = "111011" # Change this to any other 6 digit bit string to hide it

        hide_me_part_1 = hide_me[0:2] # '11'
        hide_me_part_2 = hide_me[2:4] # '10'
        hide_me_part_3 = hide_me[4:6] # '11'


        red_bits_new   = replace_last_n_bits(to_bits8(original_red_value), hide_me_part_1)   # The first two bits
        green_bits_new = replace_last_n_bits(to_bits8(original_green_value), hide_me_part_2) # Middle two
        blue_bits_new  = replace_last_n_bits(to_bits8(original_blue_value), hide_me_part_3)  #  Last Two

        new_red_value = from_bits8(red_bits_new)
        new_green_value = from_bits8(green_bits_new)
        new_blue_value = from_bits8(blue_bits_new)

        print("\nAltered Pixel (binary):")
        print("RED:",  to_bits8(new_red_value))
        print("GRN:",  to_bits8(new_green_value))
        print("BLU:",  to_bits8(new_blue_value))

        # Write back to image
        picture[column, row] = (new_red_value, new_green_value, new_blue_value)

        # Verify by reading the last n bits back using your extractor
        verifying_red, verifying_green, verifying_blue= picture[column, row]
        print("\nVerification (read last bits back):")
        print("RED LSB (n=1):", extract_last_n_bits(to_bits8(verifying_red), 2))  # expect '1'
        print("GRN LSB (n=1):", extract_last_n_bits(to_bits8(verifying_green), 2))  # expect '0'
        print("BLU LSBs(n=2):", extract_last_n_bits(to_bits8(verifying_blue), 2))  # expect '10' (as a 2-bit string)

        im.save("../docs/monalisa_altered.bmp")
        print("\nSingle Pixel Steganography Done (saved ../docs/monalisa_altered.bmp)")

except Exception as err:
    print("Steg Failed:", str(err))
