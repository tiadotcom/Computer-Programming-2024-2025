import os

def navigate_and_print(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        print(f"Directory: {dirpath}")
        for dirname in dirnames:
            print(f"  Subdirectory: {dirname}")
        for filename in filenames:
            print(f"  File: {filename}")

# Example usage
navigate_and_print(r"C:\Users\matil\OneDrive\Desktop PC Mati\uni\didactic material")
