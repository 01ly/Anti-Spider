#coding:utf-8
import re
import requests
from commons import *
from fontTools.ttLib import TTFont
from util import download_and_save


# 1. 获取店铺页面源码
def parse_and_handle_shop_page(shop_id):
    shop_source_html = requests.get(example_shop_url.format(shop_id=shop_id),headers=request_headers)
    shop_html = shop_source_html.text
    # 2. 获取svg 用 css 链接 以及 读取内容 以待获取woff字体下载链接
    svg_url = schema + re.findall(pattern_svgcss, shop_html)[0]
    svg = requests.get(svg_url)
    svgtextcss = svg.text
    return shop_html,svgtextcss

# 3. 获取加密用woff 字体，下载至本地
# 电话地址 的解密woff文件 需要的url是第一个即：
# woff_url = schema + re.findall(pattern_woff,svgtextcss)[0]
# 评论内容的解密woff文件 需要的url是第二个，即：
# woff_url = schema + re.findall(pattern_woff,svgtextcss)[1]
def download_woff(woff_path:str=woff_path,woff_xml_path:str=woff_xml_path,woff_index:int =0,svg_css=None):
    woff_url = schema + re.findall(pattern_woff,svg_css)[woff_index]
    download_and_save(woff_url,woff_path)
    # 4. 使用fontTools库解析woff字体文件，获取字体排序列表
    font = TTFont(woff_path)
    font.saveXML(woff_xml_path)
    TTGlyphs = font['cmap'].tables[0].ttFont.getGlyphOrder()[2:]
    return TTGlyphs