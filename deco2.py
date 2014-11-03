# -*- coding: cp936 -*-


def d(a):
    def _d(fp):
        def __d(*arg, **karg):
            print a
            print "do sth before fp.."
            r= fp(*arg, **karg)
            print "do sth after fp.."
            return r
        return __d
    return _d



@d("haha")
def f():
    print "call f"


@d("hehe")
def f2(a, b=2):
    print "call f2"
    print a+b


f()

print "-"*20

f2(1)

print "-"*20

f2(a=1, b=4)
