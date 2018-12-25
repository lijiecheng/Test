#！/usr/bin/python

# python 高阶函数 map和reduce函数使用
from functools import reduce

def fn(x):
    return  x**2
	
def fn1(x, y):
    return x*y

result1 = map(fn, range(1,9))
result2 = reduce(fn1, range(1, 9))

print(result1)
print(result2)