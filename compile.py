# -*- coding: utf-8 -*-

import py_compile
while 1:
    p = raw_input('Compile file----->>>')
    py_compile.compile(r''+p)
    result = raw_input('Continue------>>>y/n:')
    if result != 'y':
        break

