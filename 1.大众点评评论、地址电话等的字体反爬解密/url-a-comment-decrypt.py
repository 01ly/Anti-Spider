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

# 6. 获取要解密的评论 标签，这里是 标签<p></p>,传进解密函数
shop_page_soup = bsoup(test_html,'lxml')
comment_list_ul_tag = shop_page_soup(comment_tag_finder['url-a'][0],**comment_tag_finder['url-a'][1])[0]
comment_list_li_tags = comment_list_ul_tag(comment_tag_finder['url-a-li'][0],**comment_tag_finder['url-a-li'][1])

# 取当前页面的第一个评论作为示例
example_comment_li_tag = comment_list_li_tags[0]
comment_p = example_comment_li_tag(comment_tag_finder['url-a-p'][0],**comment_tag_finder['url-a-p'][1])[0]
print('>> 未解密评论内容：')
print(comment_p)

result = decrypt_woff_tag(comment_p,TTGlyphs,woffs)
print(f'\n>> 解密后评论内容：\n {result}')