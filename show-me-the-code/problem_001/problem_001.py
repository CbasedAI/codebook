#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
作为 Apple Store App 独立开发者，
你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
'''

import random, string

poolOfChars  = string.ascii_letters + string.digits
random_codes = lambda x, y: ''.join([random.choice(x) for i in range(y)])

i = 0

while i < 200:
    print(random_codes(poolOfChars, 15))
    i+=1