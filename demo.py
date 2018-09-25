#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#用户验证

from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_4) Applewebkit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
username = 'admin'
passwd = 'password'
url = 'https://localhost:8834/#/scans/folders/my-scans'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,passwd)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)



'''
#代理

from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
from urllib import request,parse
proxy_handler = ProxyHandler({
    'http':'http://127.0.0.1:1080',
    'https':'https://127.0.0.1:1080'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)


#cookie
import http.cookiejar,urllib.request
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

try:
    response = opener.open('https://www.baidu.com')
    #response = opener.open('https://www.google.com')
except URLError as e:
    print(e.reason)
for item in cookie:
    print(item.name+"="+item.value)



from urllib import request,error
try:
    response = request.urlopen('https://cuiqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')


#error
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://www.baudu.com',timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')



##使用requests
import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_4) Applewebkit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r=requests.get("https://www.zhihu.com/explore",headers=headers)
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)

titles=re.findall(pattern,r.text)
print(titles)

r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico','wb') as f:
    f.write(r.content)

'''