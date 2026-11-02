import os

# The least significant bits in a byte are the last ones.
# These are the ones that make the least change to the value you swap them.
# Think in base ten changing 404 to 504 makes the number change by 100 when you swap the first digit
# When you swap the last, 404 to 405 the number only changes by one.
# These small changes allow us to possibly hide data in the last bits without making too much noise.


# Bits are a string here - using the type hint :str
def extract_last_n_bits(bits: str, n=1):
    # n is defaulting to 1, but you can set it to 2 and get the last two bits and so on.
    # Extract the last n bits from every 8-bit chunk in the bitstring
    extracted = ''.join(bits[i+8-n:i+8] for i in range(0, len(bits), 8))
    return extracted

    # The above code is essentially this:
    # extracted = ""
    # for i in range(0, len(bits), 8):                 # process one byte (8 bits) at a time
    #     byte = bits[i:i+8]                           # take the 8-bit chunk
    #     extracted += byte[-n:]                       # append the last n bits (LSBs)
    #
    # return extracted

def replace_last_n_bits(bits: str, new_bits: str) -> str:
    if len(new_bits) > 8:
        raise ValueError('Too many bits cannot replace')
    if any(b not in '01' for b in new_bits):
        raise ValueError("new_bits must contain only '0' or '1'")
    if len(bits) % 8 != 0:
        raise ValueError("bitstring length must be a multiple of 8")

    n = len(new_bits)  # number of bits to replace
    # Replace the last n bits in every 8-bit chunk with the provided bits
    replaced = ''.join(bits[i:i+8-n] + new_bits for i in range(0, len(bits), 8))
    return replaced

    # The above code is essentially this:
    # replaced = ""
    # for i in range(0, len(bits), 8):              # one byte (8 bits) at a time
    #     byte = bits[i:i+8]                        # get the 8-bit chunk
    #     first_part = byte[:8-n]                   # keep the first (8-n) bits
    #     replaced += first_part + new_bits         # append your custom bits
    #
    # return replaced

if __name__ == "__main__":
    byte_example = "10110010"

    print("The least significant bit of '10110010' text is:")
    print(extract_last_n_bits(byte_example))

    print("The least significant 2 bits of '10110010' text are:")
    print(extract_last_n_bits(byte_example, 2))

    print("\nNow with a random byte\n")

    # Now with a random byte:
    random_byte = os.urandom(1)                     # This gives a random byte object
    random_int = random_byte[0]                     # convert the byte to an integer (0–255)
    byte_example = format(random_int, '08b')        # convert the integer to an 8-bit binary string

    print(f"The least significant bit of '{byte_example}' text is:")
    print(extract_last_n_bits(byte_example))

    print(f"The least significant 2 bits of '{byte_example}' text are:")
    print(extract_last_n_bits(byte_example, 2))
