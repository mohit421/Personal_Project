"""
A simple script and library to convert files or strings from DOS-like
line endings to Unix-like line endings.
"""

import argparse
import os


def str2unix(input_str: str) -> str:
    """
    Converts the string from \r\n line endings to \n
    """
    return input_str.replace('\r\n', '\n')


def dos2unix(source_file: str, dest_file: str):
    """
    Converts a file that contains DOS-like line endings into Unix-like
    """
    # Check if source file exists
    if not os.path.exists(source_file):
        print(f"❌ Error: The file '{source_file}' was not found.")
        return

    # Read the DOS-style file
    with open(source_file, 'r', encoding='utf-8') as reader:
        dos_content = reader.read()

    # Convert to Unix-style
    unix_content = str2unix(dos_content)

    # Write the converted file
    with open(dest_file, 'w', encoding='utf-8') as writer:
        writer.write(unix_content)

    print(f"✅ Converted '{source_file}' → '{dest_file}' successfully!")


if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="Script that converts a DOS-like file to a Unix-like file",
    )

    # Add required source file argument
    parser.add_argument(
        'C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt',
        help='Path to the source file to be converted (e.g., dogbreeds.txt)'
    )

    # Add optional destination file argument
    parser.add_argument(
        '--dest_file',
        help='Destination file path (default: source_file appended with `_unix`)',
        default=None
    )

    # Parse command-line arguments
    args = parser.parse_args()

    s_file = args.source_file
    d_file = args.dest_file

    # If no destination file provided, auto-generate one
    if d_file is None:
        file_path, file_extension = os.path.splitext(s_file)
        d_file = f'{file_path}_unix{file_extension}'

    dos2unix(s_file, d_file)
