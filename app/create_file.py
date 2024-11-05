import os
import sys
from datetime import datetime
from typing import List


def create_directory(path_parts: List[str]) -> str:
    """Create directories from path parts if they don't exist."""
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory created: {directory_path}")
    return directory_path


def create_file(file_path: str) -> None:
    """Create a file and append content with timestamp and line numbering."""
    with open(file_path, "a") as file:
        # Write timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1
    print(f"File created/updated: {file_path}")


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        dir_index = args.index("-d")
        path_parts = []
        for i in range(dir_index + 1, len(args)):
            if args[i] == "-f":
                break
            path_parts.append(args[i])

        # Create the directory path
        directory_path = create_directory(path_parts)
    else:
        directory_path = ""

    if "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)
    else:
        print("No file name provided. Use -f flag to specify the file.")


if __name__ == "__main__":
    main()
