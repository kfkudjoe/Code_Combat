import os
import argparse

def create_files_in_range(start, end, directory="output-files"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(start, end + 1):
        filename = f"P4_{i}.py"
        file_path = os.path.join(directory, filename)

        with open(file_path, 'w') as f:
            f.write("")
    print(f"Created {end - start + 1} files in '{directory}' directory.")

def main():
    parser = argparse.ArgumentParser(description="Create numbered files in a given range")
    parser.add_argument("start", type=int, help="Starting number of the range")
    parser.add_argument("end", type=int, help="Ending number of the range")
    parser.add_argument("-d", "--directory", type=str, default="output_files", help="Directory where files will be created (default: output_files)")
    args = parser.parse_args()

    create_files_in_range(args.start, args.end, args.directory)

if __name__ == "__main__":
    main()