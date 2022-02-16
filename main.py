import argparse
import os
from os import path, listdir
from os.path import isfile, join

def create_and_write_result(destination, filename, lines):
    with open(os.path.join(destination, filename), "w") as file:
        file.writelines("\n".join(line for line in lines))

def merge_directory_files(directory_path, destination, filename):
    files = [join(directory_path, f) for f in listdir(directory_path) if isfile(join(directory_path, f))]
    lines = []

    for file in files:
        with open(file) as tmp_file:
            lines += [line.rstrip() for line in tmp_file]

    create_and_write_result(destination, filename, lines)

def merge_mutiple_files(destination, filename, files):
    lst_files = list(files)
    lines = []

    for file in files:
        with open(file) as tmp_file:
            lines += [line.rstrip() for line in tmp_file]

    create_and_write_result(destination, filename, lines)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='split file each x lines (defined by the parameter -l)')
    parser.add_argument("-n",
                        "--filename",
                        dest="filename",
                        default="merged_files.txt",
                        help="Give the final name\n(default name: merged_file.txt)")
    parser.add_argument("-f",
                        "--files",
                        dest="files",
                        nargs='+',
                        default=[],
                        help="Give all filenames or full path of each file")
    parser.add_argument("-D",
                        "--Directory",
                        dest="directory_path",
                        help="Give the path or the name of the directory contains all your files")
    parser.add_argument(
        "-d",
        "--destination",
        default=".",
        dest="destination",
        help="specify the destination to create the new files"
    )

    args = parser.parse_args()

    if not path.exists(args.destination):
        os.makedirs(args.destination)

    if args.directory_path:
        merge_directory_files(args.directory_path, args.destination, args.filename)
    else:
        merge_mutiple_files(args.destination, args.filename, args.files)