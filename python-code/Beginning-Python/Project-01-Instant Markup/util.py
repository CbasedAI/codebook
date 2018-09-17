#!usr/bin/python
# -*- coding: utf-8 -*-

def lines(file):
    #文章末尾追加换行符
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():    #非空行
            block.append(line)
        elif block: #遇到空白行时（即文本块末尾），且block非空，则连接里面的行
            yield ''.join(block).strip()
            block = []