#codng:utf-8

import requests
import html
import re 

def download_and_save(url,save_path,mode='wb',**request_kwargs):
    with open(save_path,mode) as f:
        response = requests.get(url,**request_kwargs)
        content = response.content
        f.write(content)

def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])

def dec(a):
    c =str( re.findall(r'(.+)',a)[0].encode('raw_unicode_escape').replace(b'\\u',b''),'utf-8')
    return c