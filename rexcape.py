#!/usr/bin/env python
import re,sys
arguments = sys.argv[1:]
string = ' '.join(arguments)
print re.escape(string)