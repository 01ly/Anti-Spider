#coding:utf-8

import re 
import requests
from commons import * 
from woffs import woffs
from url_a import TTGlyphs,shop_html
from decrypt import decrypt_woff_tag
from bs4 import BeautifulSoup as bsoup

# 1-4 在 url_a.py 中

test_html = shop_html
# 如果你的IP请求被禁了，注释掉上面那行代码，页面源码可以使用下面的这两行
# 字体则需自己下载
# with open(example_shop_html_a,'rb') as f:
#     test_html = f.read()

# 5 .制作出解密用对应字体库，具体有两个思路：
# 0x01:
#       a. 可以使用百度FontEditor查看woff字体文件内容，链接：http://fontstore.baidu.com/static/editor/index.html
#       b. 而后预览，后截图，使用腾讯文字识别上传截图识别出所有文字,制作字体库woffs。详细看woffs.py
# 0x02：
#       a. 第四步的 font_a.saveXML(woff_a_to_xml) 将woff字体文件转为xml文件
#       b. 将字体xml文件中<glyf></glyf>标签中的所有<TTGlyph>标签内的name属性以及字体信息坐标获取出来，使用Matplotlib等绘图工具，根据坐标将字形轮廓绘画出来
#       c. 将绘画结果字形图片利用腾讯文字识别api进行识别，存储对应{name:文字}字典

# 6. 获取要解密的地址、电话 标签，这里是 标签<span id="address">...</span>以及标签<span class="info-name">...</span>,传进解密函数
shop_page_soup = bsoup(test_html,'lxml')

address_tag = shop_page_soup(comment_tag_finder['url-a-address'][0],**comment_tag_finder['url-a-address'][1])[0]
phone_tag = shop_page_soup(comment_tag_finder['url-a-phone'][0],**comment_tag_finder['url-a-phone'][1])[0]
print('>> 未解密地址、电话：')
print(address_tag)
print(phone_tag)

d_address = decrypt_woff_tag(address_tag,TTGlyphs,woffs)
d_phone =  decrypt_woff_tag(phone_tag,TTGlyphs,woffs)
print('>> 解密后地址、电话：')
print(f'地址：{d_address}')
print(f'电话{d_phone}')