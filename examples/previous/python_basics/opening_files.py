# Opening a file in binary mode

OPEN_ME = "_notes.txt"

print("-" * 50)
print("Opening in Read Only Mode")
mode = "r" # Read Only
with open(OPEN_ME, mode) as file:
    try:
        first_line = file.readline()
        print(first_line)
    except Exception as e:
        print(f"Could not read because: {e}")
    try:
        file.write("Can I write this in?")
        print("Write executed successfully")
    except Exception as e:
        print(f"Could not write because: {e}")

print("-" * 50)
print("Opening in Write Only Mode")
mode = "w"  # Write Mode
with open(OPEN_ME, mode) as file:
    try:
        first_line = file.readline()
        print(first_line)
    except Exception as e:
        print(f"Could not read because: {e}")
    try:
        file.write("Can I write this in?") #notice this overrides whatever was already in notes
        print("Write executed successfully")
    except Exception as e:
        print(f"Could not write because: {e}")

print("-" * 50)
print("Opening in Append Only Mode")
mode = "a"  # Append Mode
with open(OPEN_ME, mode) as file:
    try:
        first_line = file.readline()
        print(first_line)
    except Exception as e:
        print(f"Could not read because: {e}")
    try:
        file.write("\nCan I write this in?") # notice this adds to whatever was already in notes at the end
        print("Write executed successfully")
    except Exception as e:
        print(f"Could not write because: {e}")

print("-" * 50)
print("Opening in Read + Write Only Mode")
mode = "r+"  # Read + Write Mode
with open(OPEN_ME, mode) as file:
    try:
        first_line = file.readline()
        print(first_line)
    except Exception as e:
        print(f"Could not read because: {e}")
    try:
        file.write("Example files go here.") # What does this do? Append or Override?
        print("Write executed successfully")
    except Exception as e:
        print(f"Could not write because: {e}")


print("-" * 50)
print("Opening in Read + Write Only Mode")
mode = "w+"  # Write + Read Mode
with open(OPEN_ME, mode) as file:
    try:
        first_line = file.readline()
        print(first_line)
    except Exception as e:
        print(f"Could not read because: {e}")
    try:
        file.write("Example files go here.")  # What does this do? Append or Override?
        print("Write executed successfully")
    except Exception as e:
        print(f"Could not write because: {e}")

# Now Guess what mode = a+ would do?

print("-" * 50)
print("Opening in Binary Only Mode")
mode = "rb"  #adding a b at the end of the mode indicates binary
# Binary mode returns bytes, not bits. Each byte = 8 bits.
with open(OPEN_ME, mode) as file:
    try:
        first_ten_bytes = file.read(10) # First ten bytes. What happens if you do .read(10) but you were only in "r" mode?
        print(first_ten_bytes)  # Notice the print statement has the b'' wrapped around the string it indicates that it's in binary mode
        print(first_ten_bytes.hex()) # If we were in "r" mode what would happen here?
        print("Cursor position:", file.tell())

        # now if we keep reading what happens?
        first_line = file.readline() # It finishes reading the line.
        print(first_line)

    except Exception as e:
        print(f"Could not read because: {e}")
    try:
        file.write("Can I write this in?")
        print("Write executed successfully")
    except Exception as e:
        print(f"Could not write because: {e}")
