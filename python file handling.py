# File Read & Write Challenge with Error Handling

def read_and_write_file():
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read from: ")
    
    try:
        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        # Modify the content (for example, adding line numbers)
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]
        
        # Ask the user for the output filename
        output_filename = input("Enter the name of the new file to write to: ")
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"File '{input_filename}' has been successfully modified and saved as '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file '{input_filename}'.")

# Run the program
read_and_write_file()
