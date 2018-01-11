# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:12:46 2018

@author: zhangp
"""
import urllib.request
import cookielib

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(hander)
response = opener.open('http://www.baidu.com')
for item in cookie:
  print('Name =' + item.name)
  print('Value =' + item.value)