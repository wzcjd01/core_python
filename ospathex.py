#!/usr/bin/env python
from __future__ import print_function

__author__ = 'Wang Zhicheng'

import os

for tmpdir in ('/tmp', r'c:\temp'):
    if os.path.isdir(tmpdir):
        break
else:
    print('no temp directory available')
    tmpdir = ''

_cur = os.getcwd()

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print('*** current temporaty directory')
    print(cwd)

    print('*** create example directory...')
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print('*** new working dirctory:')
    print(cwd)
    print('*** original directory listing:')
    print(os.listdir(cwd))

    print('*** creating test file...')
    fobj = open('test', 'w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print('*** updated directory listing:')
    print(os.listdir(cwd))

    print("*** renaming 'test' to 'test_file.txt'")
    os.rename('test', 'test_file.txt')
    print('*** updated directory listing:')
    print(os.listdir(cwd))

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print("*** full file pathname:")
    print(path)

    print('*** (dirname, basename) ==')
    print(os.path.split(path))
    print('*** (filename, extention) ==')
    print(os.path.splitext(path))

    print('*** displaying file content')
    fobj = open(path)
    for line in fobj:
        print(line.strip())
    fobj.close()

    print('*** deleting ...')
    os.remove(path)
    os.chdir(os.pardir)
    os.rmdir('example')

    os.chdir(_cur)
    print('*** Done ***')
