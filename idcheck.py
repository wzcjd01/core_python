#__author__ = 'Wang Zhicheng'
"""
check for valid Python identifiers
"""

from string import  ascii_letters as _ascii_letters, digits as _digits
from keyword import kwlist as _kwlist

_alphas = _ascii_letters + '_'
_nums = _digits
_alphnums = _alphas + _nums

print "welcome to the identifier checker v2.0"
#print "testees must be at least 2 chars long."
ainput = raw_input("Indentifier to test? ").strip()

if len(ainput) > 1:
    if ainput[0] not in _alphas:
        print "Invalid: first symbol must be alphabetic."
    else:
        for otherchar in ainput[1:]:
            if otherchar not in _alphnums:
                print "invalid: remaining symbol must be alphanumeric."
                break
        else:
            if ainput in _kwlist:
                print "You just entered a keyword: %s" % ainput
            else:
                print "okay as an identifier."
else:
    if ainput in _ascii_letters:
        print "Okay as an identifier"
    else:
        print "invalid: single char identifier must be an ascii letter."
