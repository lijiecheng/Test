#!/usr/bin/python3
#coding: utf-8

from urllib import request

# url = 'https://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

url = 'https://httpbin.org/ip'

hander = request.ProxyHandler({"http":"121.233.207.19:9999"})

opener = request.build_opener(hander)

resp = opener.open(url)

print(resp.read())

