def read_file_with_error_handling():
    filename = input("Please enter the filename: ")
    
    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read the file '{filename}'.")

# Example usage
read_file_with_error_handling()
