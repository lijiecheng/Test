#!/usr/bin/python3
#coding: utf-8
from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

def get_opener():
    cookiejar = CookieJar()
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    return opener

def login_renren(opener):
    data = {
            'email':'1030183493@qq.com',
            'password':'19920804ljc'
            }
    login_url = "http://www.renren.com/PLogin.do"
    req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'), headers=headers)
    opener.open(req)

def visit_profile(opener):
    dapeng_url = "http://www.renren.com/880151247/profile"
    req = request.Request(dapeng_url, headers=headers)
    resp = opener.open(req)
    with open("renren.html",'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)
