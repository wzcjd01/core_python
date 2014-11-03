def d(fp):
    def _d(*arg, **karg):
        print "do sth before fp.."
        r = fp(*arg, **karg)
        print "do sth after fp.."
        return r
    return _d


@d
def f():
    print "call f"
# 上面使用@d来表示装饰器和下面是一个意思
# f = d(f)


f()      # 调用f
