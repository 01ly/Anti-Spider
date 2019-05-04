#coding:utf-8

import re
import requests
from commons import * 
from fontTools.ttLib import TTFont
from util import download_and_save

# 1. 获取店铺页面源码
shop_source_html = requests.get(example_shop_url_a,headers=request_headers)
shop_html = shop_source_html.text

# 2. 获取svg 用 css 链接 以及 读取内容 以待获取woff字体下载链接
svg_url = schema + re.findall(pattern_svgcss,shop_source_html.text)[0]
svg = requests.get(svg_url)
svgtextcss = svg.text

# 3. 获取加密用woff 字体，下载至本地
woff_url = schema + re.findall(pattern_woff,svgtextcss)[-1]
download_and_save(woff_url,woff_a_path_name)

# 4. 使用fontTools库解析woff字体文件，获取字体排序列表
font_a = TTFont(woff_a_path_name)
font_a.saveXML(woff_a_to_xml)
TTGlyphs = font_a['cmap'].tables[0].ttFont.getGlyphOrder()[2:]