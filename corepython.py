#__author__ = 'Wang Zhicheng'


class FooClass(object):
    """my very first class: FooClass"""
    version = 0.1       # class (data) attribute

    def __init__(self, nm='John Doe'):
        """constructor"""
        self.name = nm   # class instance (data) attribute
        print 'Created a class instance for', nm

    def showname(self):
        """display instance attribute and class name"""
        print 'your name is', self.name
        print 'my name is ', self.__class__.__name__

    def showver(self):
        """display class(static) attribute"""
        print 'version is ', self.version

    def addme2me(self, x):  # doses not use 'self'
        return x + x