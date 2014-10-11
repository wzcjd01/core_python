#__author__ = 'Wang Zhicheng'
"""
write an unicode string to disk and read it back in for display.
it encodes it into UTF-8 for writing to disk
"""

_codec = 'utf-8'
_file = 'unicode.txt'

_hello_out = u"Hello world\n"
_bytes_out = _hello_out.encode(_codec)

def example0602():
    f = open(_file, 'w')
    f.write(_bytes_out)
    f.close()

    f = open(_file, 'r')
    bytes_in = f.read()
    f.close()
    hello_in = bytes_in.decode(_codec)
    print hello_in,


if __name__ == "__main__":
    example0602()

