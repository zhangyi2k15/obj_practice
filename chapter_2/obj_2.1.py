#!/usr/bin/env python
# encoding: utf-8
"""
@project: obj_practice
#@ide: PyCharm
@author: zhh
@license: (C) Copyright, ZHH individual Limited.
@contact: zhangyi2k15@qq.com
@software: python
@file: obj_2.1.py
@time: 2020/1/19 9:32 下午
@desc:
"""
import math

from ecommerce.products import Product
from ecommerce import db
class Point(object):
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calc_distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

if __name__ == '__main__':

    point_1 = Point()
    point_2 = Point()
    point_1.reset()
    point_2.move(5, 0)
    print(point_2.calc_distance(point_1))
    assert (point_2.calc_distance(point_1) == point_1.calc_distance(point_2))

    point_1.move(3, 4)
    print(point_1.calc_distance(point_2))
