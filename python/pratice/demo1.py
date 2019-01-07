#!/usr/bin/python

#-*- coding: utf-8 -*-

"""
1, 2, 3, 4 这四个数字，能组成多少个互不相同且无重复的三位数字，各是多少

"""
def example1():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
    	        if (i != j) and (i != k) and (j != k):
    		        print(i,j,k)

def example2():
    import itertools
    myList = list(itertools.permulations([1,2,3,4],3))
    print(myList)
