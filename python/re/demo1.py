#! /usr/bin/python
# coding: utf-8
"""
.          匹配任意字符
[...]      匹配任意字符集
"""


import re
str1 = "imooc python"
pa = re.compile(r'imooc')
ma = pa.match(str1)
print(ma.group())

str2 = "hello python"
ma = re.match(r'hello', str2)
print(ma.group())