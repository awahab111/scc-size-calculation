import os
import scc

# Ask the user for the input file name
filename = input("Enter the name of the input file: ")

# Check if the file exists
if not os.path.isfile(filename):
    print("File not found!")
else:
    # Process the input file
    print("Processing", filename, "...")
    print("Nodes in largest SCC:")
    print(scc.largest_scc(filename))
