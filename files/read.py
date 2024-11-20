def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, "r") as file:
            content = file.read()
        
        # Modify the content (for example, converting to uppercase)
        modified_content = content.upper()
        
        # Open the output file in write mode and write the modified content
        with open(output_filename, "w") as file:
            file.write(modified_content)
        
        print(f"File content successfully written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read or write the file.")

# Example usage
input_file = "input.txt"  # Change to your file path
output_file = "output.txt"  # Change to your desired output file path
read_and_write_file(input_file, output_file)
