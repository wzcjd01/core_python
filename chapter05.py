# __author__ = 'Wang Zhicheng'

import math


def _test():
    for eachNum in (.2, .7, 1.2, 1.7, -.2, -.7, -1.2, -1.7):
        print "int(%.1f)\t%+.1f" % (eachNum, float(int(eachNum)))
        print "floor(%.1f)\t%+.1f" % (eachNum, math.floor(eachNum))
        print "round(%.1f)\t%+.1f" % (eachNum, round(eachNum))
        print '-' * 20


if __name__ == '__main__':
    _test()