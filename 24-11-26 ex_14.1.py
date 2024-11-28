# Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames;
# it should read the first file and write the contents into the second file (creating it if necessary). 
# If the pattern string appears anywhere in the file, it should be replaced with the replacement string.

def sed(pattern_string, replacement_string, filename1, filename2):
    try: 
        file1 = open(filename1, "r")
        file2 = open(filename2, "w")
        for line in file1:
            updated_line = line.replace(pattern_string, replacement_string)
            file2.write(updated_line)

    except FileNotFoundError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        # Ensure the files are properly closed
        if 'file1' in locals() and not file1.closed:
            file1.close()
        if 'file2' in locals() and not file2.closed:
            file2.close()

    # Prints file2
    try:
        file2 = open(filename2, "r")
        for line in file2:
            print(line, end="")
    finally:
        if 'file2' in locals() and not file2.closed:
            file2.close()

# empty.txt
sed("university", "fuck", "sample.txt", "empty.txt")
