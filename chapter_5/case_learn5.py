#!/usr/bin/env python
# encoding: utf-8
"""
@project: obj_practice
#@ide: PyCharm
@author: zhh
@license: (C) Copyright, ZHH individual Limited.
@contact: zhangyi2k15@qq.com
@software: python
@file: case_learn5.py
@time: 2020/2/6 5:57 下午
@desc:
"""
class Document:
    def __init__(self):
        self.characters = []
        self.cursor = 0
        self.filename = ''

    def insert(self, character):
        self.characters.insert(self.cursor, character)
        self.cursor += 1

    def delete(self):
        del self.characters[self.cursor]

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    def forward(self):
        self.cursor += 1

    def back(self):
         self.cursor -= 1


class Cursor:
    def __init__(self, document):
        self.document = document  # 保存document的目的是 home 和 end 函数的操作
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        while self.position < len(self.document.characters) and \
                self.document.characters[self.position].character != '\n':
            self.position += 1

class Document2:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)  # 将Document2 设置为Cursor的document
        self.filename = ''

    def insert(self, character):
        if not hasattr(character, 'character'): #  用于判断对象是否包含属性
            character = Character(character)  #  表示一个对象
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))

class Character:
    def __init__(self, character, bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return bold + italic + underline + self.character

if __name__ == '__main__':
    d = Document2()
