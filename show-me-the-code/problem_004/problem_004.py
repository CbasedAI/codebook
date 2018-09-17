#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
第 0004 题：
任一个英文的纯文本文件，统计其中的单词出现的个数,行数,字符数
'''

from collections import Counter

try:
    file_name = input("Pleasr input your filename,including its suffix:")
    #file_name = 'test.txt'

    lines_count = 0
    words_count = 0
    chars_count = 0

    with open(file_name,'r') as f:
        for line in f:
            words = line.split()

            lines_count += 1
            chars_count += len(line)
            words_count += len(words)

    print('lines_count is :', lines_count)
    print('chars_count is :', chars_count)
    print('words_count is :', words_count)

except (FileNotFoundError):
    print("It couldn't found the file, please try again.")



