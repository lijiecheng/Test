#!/usr/bin/python3
#coding;utf-8

from urllib import request
from urllib import parse

url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
       "Referer":"https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
       "X-Requested-With":"XMLHttpRequest",
       "Accept": "application/json, text/javascript, */*; q=0.01",
       "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8'
       }

data = {
        "first": "true",
        "pn": "1",
        "kd": "python"
        }


req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method ="POST")
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
