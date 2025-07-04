def process_file(input_file_path, output_file_path):
    try:
        # Attempt to open and read the input file
        with open(input_file_path, 'r') as infile:
            data = infile.read()
        
        # Process the data to count lines, words, and characters
        lines = data.splitlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_characters = len(data)
        
        # Write the processed data to the output file
        with open(output_file_path, 'w') as outfile:
            outfile.write(f"Number of lines: {num_lines}\n")
            outfile.write(f"Number of words: {num_words}\n")
            outfile.write(f"Number of characters: {num_characters}\n")
        
        print(f"Processing completed successfully. Results are saved in {output_file_path}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{input_file_path}' or '{output_file_path}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
