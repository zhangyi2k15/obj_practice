#!/usr/bin/env python
# encoding: utf-8
"""
@project: obj_practice
#@ide: PyCharm
@author: zhh
@license: (C) Copyright, ZHH individual Limited.
@contact: zhangyi2k15@qq.com
@software: python
@file: obj_5.py
@time: 2020/2/6 10:56 上午
@desc:
"""

# 通过属性向类数据添加行为


class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception('Invalid Name')
        self._name = name

    def _get_name(self):

        return self._name
    name = property(_get_name, _set_name)  #  创建一个name属性，取代之前的name属性


#  上面代码的重写
class Color2:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise Exception('Invalid Name')
        self._name = name

#  决定合适使用属性
from urllib.request import urlopen
import time

class WebPage:
    def __init__(self, url):
        self.url = url
        self._context = None

    @property
    def content(self):
        if not self._context:
            print('Retrieving New Page....')
            self._context = urlopen(self.url).read()

        return self._context


#  管理员对象
import sys
import shutil
import zipfile
from pathlib import Path


# class ZipReplace:
#     def __init__(self, filename, search_string, replace_string):
#         self.filename = filename
#         self.search_string = search_string
#         self.replace_string = replace_string
#         self.temp_directory = Path(f'unzipped-{filename}')
#
#     def zip_find_replace(self):
#     #   流程管理
#         self.unzip_files()
#         self.find_replace()
#         self.zip_files()
#
#     def unzip_files(self):
#         self.temp_directory.mkdir()
#         with zipfile.ZipFile(self.filename) as zip:
#             zip.extractall(str(self.temp_directory))
#
#     def find_replace(self):
#         for filename in self.temp_directory.iterdir():
#             with filename.open() as file:
#                 contents = file.read()
#             contents = contents.replace(self.search_string, self.replace_string)  # 替换文件名
#             with filename.open('w') as file:
#                 file.write(contents)
#
#     def zip_files(self):
#         with zipfile.ZipFile(self.filename, 'w') as file:
#             for filename in self.temp_directory.iterdir():
#                 file.write(str(filename), filename.name)
#
#         shutil.rmtree(str(self.temp_directory))  # 递归删除文件及文件目录

#  实践
class ZipProcessor:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = Path(f'unzipped-{zipname[:4]}')

    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))


    def process_files(self):
        pass

    def zip_files(self):
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)

        shutil.rmtree(str(self.temp_directory))  # 递归删除文件及文件目录


class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)

            with filename.open('w') as file:
                file.write(contents)


from PIL import Image
class ScaleZip(ZipProcessor):

    def process_files(self):
        """
        scale each image in the directory to 680*480
        :return:
        """
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((630, 480))
            scaled.save(str(filename))


if __name__ == '__main__':
    c = Color('#000ff', 'red')
    print(c.name)

    webpage = WebPage('https://www.zhihu.com/')
    now = time.time()
    content1 = webpage.content
    time.time() - now
