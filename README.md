# gddown.py
A python wrapper for gdrive-org/gdrive that allows easy access to downloading
files based on their path.

## Getting Started

### Installing

To use this, you need to download the [gdrive](https://github.com/gdrive-org/gdrive)
CLI tool and put the executable onto your path.

Then, download this script and run it to download files.

### Running

To run, execute:
```
python3 gddown.py path/to/file/in/google/drive/to/download
```

You can use a `*` to download all files in a directory, such as:
```
python3 gddown.py folder/to/download/all/files/*
```
or to specify downloading from all subdirectories of a given directory, such as:
```
python3 gddown.py path/to/folder/*/file
```
A `*` may also be placed at the end of a name to specify a prefix to download
all files to match, such as:
```
python3 gddown.py path/to/files/with/prefix*
```

You can specify multiple files in one command and it will download all of them,
such as:
```
python3 gddown.py path/to/file/in/google/drive/to/download path/to/other/file
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
