##  Example of working with text and converting it to bits and vice versa

def convert_text_to_bits(text) -> str:
    text_to_convert = text.encode('utf-8')
    bits = ''.join(format(byte, '08b') for byte in text_to_convert)
    return bits

    # The above code is essentially this:
    # text_to_convert = text.encode('utf-8')
    # bits = ""
    # for byte in text_to_convert:
    #     bits += format(byte, '08b')
    #
    # return bits


def convert_bits_to_text(bits) -> str:
    bytes_list = [int(bits[i:i + 8], 2) for i in range(0, len(bits), 8)]
    text = bytes(bytes_list).decode('utf-8')
    return text

    # The above code is essentially this:
    # bytes_list = []
    # for i in range(0, len(bits), 8):
    #     byte = int(bits[i:i+8], 2)
    #     bytes_list.append(byte)
    #
    # text = bytes(bytes_list).decode('utf-8')
    # return text


if __name__ == '__main__':
    text = input("What text would you like to convert?")
    if not text:
        text = "Violent Python is my favorite course!"
        print(f"\nNo input detected - automatically converting the default text:\n{text}\n")

    bits = convert_text_to_bits(text)
    print("Your converted encoded text is:")
    print(bits)
    print("\nNow let's convert it back to text!\n")
    print("Your decoded text is:")
    print(convert_bits_to_text(bits))