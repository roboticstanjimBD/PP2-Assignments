import os
import shutil

# Create a source directory
os.makedirs("Source", exist_ok=True)

# Create a destination directory
os.makedirs("Destination", exist_ok=True)

# Create a sample file
with open("Source/example.txt", "w") as file:
    file.write("This is a sample file.")

# Move the file to the destination folder
shutil.move("Source/example.txt", "Destination/example.txt")

print("File moved successfully.")
