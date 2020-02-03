#!/usr/bin/env python
# encoding: utf-8
"""
@project: obj_practice
#@ide: PyCharm
@author: zhh
@license: (C) Copyright, ZHH individual Limited.
@contact: zhangyi2k15@qq.com
@software: python
@file: contact.py
@time: 2020/1/20 9:38 下午
@desc:
"""

# ========  基本的继承
class Contact(object):
    all_contacts = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Suplier(Contact):
    def order(self, order):
        print(f'if this were a real system we would send {order} to {self.name}')

# ======扩展内置对象
class ContractList(list):  # 对list对象扩展一个search功能
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:  # 仅仅是字符串的匹配
                matching_contacts.append(contact)
        return matching_contacts

class Contact(object):
    all_contacts = ContractList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

c1 = Contact('john A', 'johnA@example.net')
c2 = Contact('john B', 'johnB@example.net')
c3 = Contact('jehna C', 'johnB@example.net')
print([c.name for c in Contact.all_contacts.search('john')])


class LongNameDict(dict): # 扩展dict类
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key

        return longest


#  重写和super
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


# 多重继承
class MailSender(object):
    def send_email(self, msg):
        print('sending mail to ' + self.email)


class EmailableContact(Contact, MailSender):
    pass

class AddressHolder(object):
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code

e = EmailableContact('john smith', 'jsmith@example.net')
e.send_email('hello, test email send here')


#==== 钻石型继承
class Friend(Contact, AddressHolder):
    def __init__(
            self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone

#  不同集合的参数
class Contact(object):
    all_contacts = []
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class AddressHolder(object):
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self, phone, **kwargs):
        super().__init__(**kwargs)
        self.phone = phone


#  抽象基类
from collections import Container

class OddContrainer(object):
    def __contains__(self, item):
        if not isinstance(item, int) or not item % 2:
            return False
        return True

odd_container = OddContrainer()
isinstance(odd_container, Container)
issubclass(OddContrainer, Container)

if __name__ == '__main__':
    # longkeys = LongNameDict()
    pass
