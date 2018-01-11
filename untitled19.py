# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:30:48 2018

@author: zhangp
"""

import os.path
import urllib.request
#import cookielib
COOKIEFILE = 'cookies.lwp'
cj = None
ClientCookie = None
cookielib = None

try:
  import cookielib
except ImportError:
  try:
    import ClientCookie
  except ImportError:
    urlopen = urllib.request.urlopen
    Request = urllib.request.Request
  else:
    urlopen = ClinetCookie.urlopen
    Request = ClientCookie.Request
    cj = ClientCookie.LWPCookieJar()


print(cookielib)
print(urlopen)
print(Request)