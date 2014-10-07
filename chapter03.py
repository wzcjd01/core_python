__author__ = 'Wang Zhicheng'

import os


def make_text_file():
        # get filename
    while True:
        fname = raw_input('Enter file name: ')
        if os.path.exists(fname):
            print "Error: '%s' already exists" % fname
        else:
            break

    # get file content lines
    lines = []
    print "\nEnter lines ('.' by itself to quit).\n"

    while True:
        entry = raw_input('>')
        if entry == '.':
            break
        else:
            lines.append(entry)

    # write lines to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.write('\n'.join(lines))
    fobj.close()
    print 'Done!'


def read_text_file():
    # get the filename
    fname = raw_input("Enter filename: ")
    print

    # attempt to open file for reading
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** file open error: ", e
    else:
        for eachLine in fobj:
            print eachLine,
            #print eachLine.strip('\n ')
        fobj.close()

if __name__ == '__main__':
    print "\nWhat you want to do?\n"
    print "(M)ake text file"
    print "(R)ead text file\n"
    option = raw_input('Select: >> ')

    if option.lower() == 'm':
        make_text_file()
    else:
        read_text_file()