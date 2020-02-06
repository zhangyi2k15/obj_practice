#!/usr/bin/env python
# encoding: utf-8
"""
@project: obj_practice
#@ide: PyCharm
@author: zhh
@license: (C) Copyright, ZHH individual Limited.
@contact: zhangyi2k15@qq.com
@software: python
@file: obj_4.py
@time: 2020/2/3 10:31 下午
@desc:
"""

#  抛出一个异常
class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError('only integers can be added')
        if integer % 2:
            raise ValueError('Only even numbers can be added')

        super().append(integer)  # 继承list 的append 方法


#  处理异常

def funny_division(divider):
    try:
        return 100 / divider
    except ZeroDivisionError:
        return 'zero is not a good idea'


def funny_division2(anumber):
    try:
        if anumber == 13:
            raise ValueError('13 is an unlucky number')
        return  100 / anumber
    except (TypeError, ZeroDivisionError):
        return 'enter a number other than zero'


def funny_division3(a_number):
    try:
        if a_number == 13:
            raise ValueError('13 is an unlucky number')
        return 100 / a_number
    except TypeError as te:
        print(f'type error {te.args}')
        return 'enter a numerical value'
    except ZeroDivisionError:
        return 'enter a number other than zero'
    except ValueError:
        print('NO, not 13 !')
        raise


#  定义我们自己的异常
class InvalidWIthdrawal(Exception):
    pass

class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__(f'account does not have {amount}')
        self.balance = balance
        self.amount = amount

    def overage(self):
        return  self.amount - self.balance


def divide_with_exception(number, divisor):
    try:
        print(f'{number} / {divisor} = {number / divisor }')
    except ZeroDivisionError:
        print(' u can not divide by zero')

def divide_with_if(number, divisor):
    if divisor == 0:
        print(' u can not divide by zero')
    else:
        print(f'{number} / {divisor} = {number / divisor }')


class Inventory(object):
    def lock(self, item_type):
        pass

    def unlock(self, item_type):
        pass

    def purchase(self, item_type):
        pass



if __name__ == '__main__':
    e = EvenOnly()

    try:
        raise InvalidWIthdrawal(20, 50)
    except InvalidWIthdrawal as e:
        print('i am so sorry')


