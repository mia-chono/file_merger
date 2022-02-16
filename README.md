# File merger
Merge multiple text files into one.
You can give several files path or directly give dir path with all your text files.

## Console Help
```
usage: main.py [-h] [-n FILENAME] [-f FILES [FILES ...]] [-D DIRECTORY_PATH] [-d DESTINATION]

split file each x lines (defined by the parameter -l)

options:
  -h, --help            show this help message and exit
  -n FILENAME, --filename FILENAME
                        Give the final name (default name: merged_file.txt)
  -f FILES [FILES ...], --files FILES [FILES ...]
                        Give all filenames or full path of each file
  -D DIRECTORY_PATH, --Directory DIRECTORY_PATH
                        Give the path or the name of the directory contains all your files
  -d DESTINATION, --destination DESTINATION
                        specify the destination to create the new files
```
