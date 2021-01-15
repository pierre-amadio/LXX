#!/usr/bin/env python3
import sys, re

s=sys.stdin.read()

rec=re.compile('(\t\t<verse osisID=".*?\.1">)(\s+)(<title.*?title>)')

def repl(k): return k.group(3)+k.group(2)+k.group(1)
s=rec.sub(repl,s)
print(s,end='')
