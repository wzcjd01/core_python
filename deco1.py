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
# ����ʹ��@d����ʾװ������������һ����˼
# f = d(f)


f()      # ����f
