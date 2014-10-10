#__author__ = 'Wang Zhicheng'
"""
check for valid Python identifiers
"""

from string import  ascii_letters as _ascii_letters, digits as _digits

_alphas = _ascii_letters + '_'
_nums = _digits

print "welcome to the identifier checker v1.0"
print "testees must be at least 2 chars long."
ainput = raw_input("Indentifier to test? ")

if len(ainput) > 1:
    if ainput[0] not in _alphas:
        print "Invalid: first symbol must be alphabetic."
    else:
        _alphnums = _alphas + _nums
        for otherchar in ainput[1:]:
            if otherchar not in _alphnums:
                print "invalid: remaining symbol must be alphanumeric."
                break
        else:
            print "okay as an identifier."

