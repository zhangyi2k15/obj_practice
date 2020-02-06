#!/usr/bin/env python
# encoding: utf-8
"""
@project: obj_practice
#@ide: PyCharm
@author: zhh
@license: (C) Copyright, ZHH individual Limited.
@contact: zhangyi2k15@qq.com
@software: python
@file: case_learn4.py
@time: 2020/2/4 9:32 下午
@desc:
"""
import hashlib


#  定义异常
class AuthExeption(Exception):
    def __init__(self, username, user=None):  # user 是一个User类
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthExeption):
    pass


class PasswordTooShort(AuthExeption):
    pass


class InvalidUsername(AuthExeption):
    pass


class InvalidPassword(AuthExeption):
    pass


class NotLoggedError(AuthExeption):
    pass


class NotpermissionError(AuthExeption):
    pass


#  定义异常结束

class User:
    def __init__(self, username, password):
        """
        create a new user object the password will be encrypted before  storing
        :param username:
        :param password:
        """
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        hash_string = (self.username + password)
        hash_string = hash_string.encode('utf8')

        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        encrypted = self._encrypt_pw(password)

        return encrypted == self.password


class Authenticator:
    def __init__(self):
        self.users = {}  # users 是关于 username ： User的字典

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)

        if len(password) < 6:
            raise PasswordTooShort(username)

        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in

        return False


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permission = {}

    def add_permission(self, perm_name):
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            self.permission[perm_name] = set()
        else:
            raise PermissionError('permission exists')

    def permit_user(self, perm_name, username):
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError('permission does not exist')
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedError(username)
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError('permission does not exist')
        else:
            if username not in perm_set:
                raise NotpermissionError(username)
            else:
                return True


if __name__ == '__main__':
    authenticator = Authenticator()
    authotizor = Authorizor(authenticator)
