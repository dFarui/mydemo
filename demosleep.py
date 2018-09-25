#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
import requests

headers = {
    'Cookie':'_xsrf=uiX4yJajh7rxqx9TO4JvwCAznfZsNLtP; d_c0="AIDkbFDW4A2PTgKp08ZxQZd4IMJjOQuWvks=|1531206866"; _zap=83139943-6f4f-4f24-bf70-a8adb3595677; l_cap_id="MDFhNTVjNWFmMjU0NGM5Yjg3NTIyZDJhNWM0OWJiNGU=|1535618864|4cacc27864ca87fa2c710da6ec8cc29c7d67916c"; r_cap_id="Zjk3NThkZTRiMDRjNGFhNTk2MDYyN2FhZDE1ODNmMjQ=|1535618864|02c69f0049ca074be69a6e749250d2e2567952d3"; cap_id="Y2U3YjI0MTU3YWFkNGJhMDg4YzUwMTQ2YzE1NjQ0MDE=|1535618864|7b41928c4682a0eb0dc8e72aac009fbde1291aaf"; tgw_l7_route=1c2b7f9548c57cd7d5a535ac4812e20e; q_c1=b21f15fd4fa848f3a2bfb15a4ccddbdc|1536140114000|1531206866000; capsion_ticket="2|1:0|10:1536140274|14:capsion_ticket|44:ZWI0Yjc2ZGNjNjY2NDFhNjgxZjY5ZDhiYzExZTBmODQ=|fa69084d0dad52fc89e843da907180a139585605b78a98c13eb38c55fbec14f6"; z_c0="2|1:0|10:1536140282|4:z_c0|92:Mi4xZ3BEcUFnQUFBQUFBZ09Sc1VOYmdEU1lBQUFCZ0FsVk4tdkY4WEFCdl9wdzZkQXNjNnRtWFBncUlGOFFFS05ZVjN3|a7e435dbc8f701e417473b8eca64332940466e72535fa9c731be1200e460f2a5"',
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_4) Applewebkit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}


r = requests.get('https://www.jianshu.com',headers=headers)
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)

###上传文件
files = {'file' : open('favicon.ico','rb')}
r = requests.post("http://httpbin.org/post",files=files)
print(r.text)


ra= requests.get('https://www.zhihu.com',headers=headers)
print(ra.text)

'''

'''
import requests
requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)


import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

import requests

proxies = {
    "http":"http://127.0.0.1:1080",
    "https":"https://127.0.0.1:1080"
}

ra = requests.get("https://www.google.com",proxies=proxies)
for key,value in ra.cookies.items():
    print(key+"="+value)



import requests
import urllib3

urllib3.disable_warnings()
response = requests.get('https://www.zhihu.com/',verify=False)

print(response.status_code)



import re
content = 'xxxxxxxx'
result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
print(result)
print(result.group(1))
print(result.span())



import re
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com',content)
print(result)



import re
content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
result = re.search('Hello.*?(\d+).*?Demo',content)
print(result)
print(result.group(1))

'''


import re
html='''<div id="songs-list">
<h2 class ＝"title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2"一路上有你<li>
<li data-view="7”>
<a href ="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐泰">往事随风 </a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">尤辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.pem" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

'''
#result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
#if result:
#    print(result.group(1),result.group(2))
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(results)
print(type(results))
for result in results:
    print(result[0],results[1],result[2])
'''
content = '54ak54fjvn56ncdjj33l'
content = re.sub('\D+','',content)
print(content)