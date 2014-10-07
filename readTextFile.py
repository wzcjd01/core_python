__author__ = 'Wang Zhicheng'

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
    fobj.close()
