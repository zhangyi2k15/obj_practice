#!/usr/bin/env python
# encoding: utf-8
"""
@project: obj_practice
#@ide: PyCharm
@author: zhh
@license: (C) Copyright, ZHH individual Limited.
@contact: zhangyi2k15@qq.com
@software: python
@file: case_learn4_editor.py
@time: 2020/2/5 11:41 上午
@desc:
"""
import case_learn4 as auth

auth.Authenticator().add_user('joe', 'joepassword')
auth.Authorizor().add_permission('test program')
auth.Authorizor().add_permission('change program')
auth.Authorizor().permit_user('test program', 'joe')


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            'login': self.login,
            'test': self.test,
            'change': self.change,
            'quit': self.quit
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input('username: ')
            password = input('password: ')
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print('the username does not exist')
            except auth.InvalidPassword:
                print('invalid password')
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            auth.authenticator.check_permission(permission, self.username)
        except auth.NotLoggedError as e:
            print(f'{e.username} is not logged in ')
            return False
        except auth.NotpermissionError as e:
            print(f'{e.username} cannot {permission}')
            return False
        else:
            return True

    def test(self):
        if self.is_permitted('test program'):
            print('testing program now....')

    def change(self):
        if self.is_permitted('change program'):
            print('changing program now....')

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ''
            while True:
                print("""
                please enter a command:
                \tlogin\tLogin
                \ttest\tTest the program
                \tchange\t Change the program
                \tquit\tQuit
                """)
                answer = input('enter a command: ').lower()
                try:
                    func = self.menu_map(answer)
                except KeyError:
                    print(f'{answer} is not a valid option')
                else:
                    func()
        finally:
            print('thanks for testing the auth module')


if __name__ == '__main__':
    Editor().menu()
