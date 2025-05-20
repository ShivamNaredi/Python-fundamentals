#File I/O
# Python can be used to perform operations on a file

# File I/O Modes in Python (Used with open() function)
# -----------------------------------------------------

# Basic Modes:
# 'r'  -> Read mode (default). File must exist.
# 'w'  -> Write mode. Overwrites file or creates if not exists.
# 'x'  -> Exclusive creation. Fails if file already exists.
# 'a'  -> Append mode. Writes to the end of file. Creates if not exists.

# Text/Binary Modes:
# 't'  -> Text mode (default). Reads/writes strings.
# 'b'  -> Binary mode. Reads/writes bytes (used for files like images, PDFs).

# Read/Write Combo:
# '+'  -> Read and Write mode. Can be combined with 'r', 'w', 'a', or 'x'.

# Combined Modes Examples:
# 'rt'   -> Read text file (default)
# 'rb'   -> Read binary file
# 'wt'   -> Write text file (overwrite or create)
# 'wb'   -> Write binary file
# 'r+'   -> Read and write (file must exist)
# 'w+'   -> Write and read (creates or overwrites file)
# 'a+'   -> Append and read (creates if not exists)
# 'x+'   -> Exclusive creation + read/write (fails if file exists)
# 'rb+'  -> Read and write binary
# 'wb+'  -> Write and read binary

# Example Usage:
# with open("file.txt", "r") as f:
#     content = f.read()

# with open("image.png", "wb") as f:
#     f.write(b'binary_data')

# with open("log.txt", "a") as f:
#     f.write("New entry\n")


f = open( "demo.txt" , "a")

# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)


f.close()


#If we want to create a file you can open it under write mode or append mode and 
#Give the file a name it will create it for you 
g = open("sample.txt" , "w+")
print(g.read())
g.write("ABCD")
g.close()


#with syntax
with open("demo.txt" , "r") as f:
    data = f.read()
    print(data)
    
#Deleting a file 
#Modules(like a code library) is a file 
#by another programmer that generally has a funtions we can use 
import os 
os.remove("sample.txt")

with open("demo.txt" , "r") as f:
    data = f.read()
new_data = data.replace("Java" , "Python")
print(data)    

with open("demo.txt" , "w") as f:
    f.write(new_data)