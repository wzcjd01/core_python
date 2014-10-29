#!/ur/bin/env python


class Time60(object):

    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def __str__(self):
        return '%d:%d' % (self.hr, self.min)

    __repr__ = __str__

    def __add__(self, other):
        return self.__class__(self.hr + other.hr +
                              (self.min + other.min) // 60,
                              (self.min + other.min) % 60)

    def __iadd__(self, other):
        self.min += other.min
        self.min %= 60
        self.hr += other.hr
        self.hr += self.min // 60
