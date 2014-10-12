__author__ = 'Wang Zhicheng'
# # page 80, example 3.1
"""
This application prompts the user for a (nonexistent) filename,
then has the user enter each line of that file. Finally, it
write the entire text file to disk
"""
import os


def _test():
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


if __name__ == '__main__':
    _test()