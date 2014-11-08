#!/usr/bin/env python
"""Parse the output of the DOS tasklist command
"""

import os
import re

with os.popen('C:/Windows/System32/tasklist.exe /nh', 'r') as f:
    for eachLine in f:
        print re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',
                         eachLine.rstrip())
