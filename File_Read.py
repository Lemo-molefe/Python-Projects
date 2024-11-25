# File Read and Write Program
try:
    # Ask the user for the filename to read
    source_file = input("Enter the name of the file to read from: ")
    with open(source_file, 'r') as file:
        content = file.read()

    # Modify the content
    modified_content = content.upper()

    # Write to a new file
    new_file = "modified_" + source_file
    with open(new_file, 'w') as file:
        file.write(modified_content)

    print(f"Content successfully modified and written to {new_file}!")

except FileNotFoundError:
    print("Error: The file you specified does not exist.")
except IOError:
    print("Error: Unable to read/write the file.")
