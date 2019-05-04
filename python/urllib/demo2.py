#!/usr/bin/python3
# coding : utf-8 
from urllib import request
from urllib import parse
url = "http://www.baidu.com/s?wd=python"

data = parse.urlparse(url)
print(data)
print("scheme :",data.scheme)
print("netloc :", data.netloc)
print("path :", data.path)
print("oarams :", data.params)
print("query: ", data.query)
print("fragment :", data.fragment)
request= parse.urlsplit(url)
print(request)
print("scheme :", request.scheme)
print("netloc :", request.netloc)
print("path :", request.path)
#print("oarams :", request.params)
print("query: ", request.query)
print("fragment :", request.fragment)



