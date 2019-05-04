#!/usr/bin/python3

from urllib import request
from urllib import parse
'''
request.urlopen() 获取url内容
'''
# resp = request.urlopen("http://www.baidu.com")

# print(resp.read().decode("utf-8"))

'''
request.urlretrieve() 获取url图片并下载
'''
# request.urlretrieve("http://www.baidu.com",'baidu.html')

'''
parse.urlencode() 编码转化
'''
# params = {"name":"张三", "age":18, "greet":"hello world"}

# result = parse.urlencode(params)
# print(result)

# url = "http://www.baidu.com/s"

# params = {"wd":"刘德华"}
# qs = parse.urlencode(params)
# url = url + "?" + qs
# resp = request.urlopen(url)
# print(resp.read())

'''
parse.parse_qs() 编码转换
'''
# data = {"name":"张三", "age":"28"}
# result = parse.urlencode(data)
# print(result)
# qs = parse.parse_qs(result)
# print(qs)
