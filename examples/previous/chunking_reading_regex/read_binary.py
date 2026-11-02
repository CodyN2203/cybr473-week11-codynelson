"""
Reading Binary Files in Chunks
"""

from binascii import hexlify


CHUNK_SIZE = 40

with open("../dumps/test.bin", "rb") as binary_file:
    while True:
        chunk = binary_file.read(CHUNK_SIZE)
        if not chunk:
            break

        print(hexlify(chunk))


print("Script Ended")
