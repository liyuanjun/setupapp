#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-5-12 下午1:33
# @Author         : Tom.Lee
# @Description    : 
# @File           : setup.py
# @Product        : PyCharm
from setuptools import setup, find_packages

setup(
    name='setupapp',
    version='1.0.0',
    author='tom.lee',
    url='https://github.com/amlyj/setupapp',
    description='simple demo for python setup',
    license="MIT",
    packages=find_packages(),
    entry_points={
        # console_scripts  输出脚本文件
        # setupapp         输出脚本文件名称
        # applib.bin:run   模块名:函数名　
        'console_scripts': ['setupapp = applib.bin:run']
    },
)
