#!/usr/bin/python
#coding: utf-8

"""
有两个磁盘文件A和B，各行存放一行字母，要求把这两个文件中的信息合并（按字母顺序排列），输出到一个新文件C中

"""

if __name__ =='__main__':
    fp = open("test1.txt")
    a = fp.read()
    fp.close()
    fp = open("test2.txt")
    b = fp.read()
    fp.close()
    fp = open("test3.txt","w")
    l = list(a + b)
    l.sort()
    s = ""
    s = s.join(l)
    fp.write(s)
    fp.close()
