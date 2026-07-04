import os

# Create a directory named "Students"
os.mkdir("Students")

print("Directory 'Students' created successfully.")

# Create nested directories
os.makedirs("Projects/Python/Assignment", exist_ok=True)

print("Nested directories created successfully.")

# List all files and directories in the current folder
print("\nContents of the current directory:")

for item in os.listdir():
    print(item)
