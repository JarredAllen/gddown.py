#!/usr/local/bin/python3.7

from sys import argv
import os, os.path
from pathlib import PurePath
from subprocess import Popen, PIPE

def download(path, root=None, skip=True):
    skip = '-s' if skip else '-f'
    print(path, path.parts)
    base = path.parts[0]
    print(f'At {base} from {root}...', end=' ')
    query = []
    if root is None:
        root = 'root'
    query.append(f"'{root}' in parents")
    if base != '*':
        if '*' in base:
            query.append(f"name contains '{base.strip('*')}'")
        else:
            query.append(f"name = '{base}'")
    query = ' and '.join(query)
    if len(path.parts) == 1:
        print('Downloading...')
        process = Popen(f'gdrive download {skip} query " {query} "', shell=True)
        process.wait()
    else:
        print('Recursing...')
        child = PurePath(os.path.join(*path.parts[1:]))
        process = Popen(f'gdrive list --query " {query} "',
                        stdout=PIPE, shell=True).stdout
        process.readline()
        for line in process:
            download(child, line.decode().split()[0])

def main(files):
    """Download the files in files"""
    for f in files:
        download(PurePath(f))

if __name__ == '__main__':
    main(argv[1:])

