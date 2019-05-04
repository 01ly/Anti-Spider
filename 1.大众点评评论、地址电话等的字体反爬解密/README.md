# 大众点评 字体反爬

## 实时更新：
 1. **2019-05-04** :
>  * 访问的店铺url示例：
>  > * (url-a) http://www.dianping.com/shop/2832061
>  > * (url-b) http://www.dianping.com/shop/15960860/review_all
>  * 更新内容:
>  > * 针对url-a 的访问页面进行 **地址**、**电话** 的woff字体反爬解密
>  > * 针对url-a 的访问页面进行 **点评评论** 的woff字体反爬解密
>  > * 针对url-b 的访问页面进行 **地址**、**电话**的svg反爬解密(详见github库: [01ly/DPSpider](https://github.com/01ly/DPspider))
>  > * 针对url-b 的访问页面进行 **点评评论** 的woff字体反爬解密(与url-a的解密一致)

## 示例(2019年5月4日版 web大众点评)

* 解密当前woff字体显示的加密评论：
` python url-a-comment-decrypt.py`
* 解密当前woff字体显示的加密电话、地址：
` python url-a-addr-phone-decrypt.py`

## 反爬点

* 使用woff字体前端显示 出现html 的NCR转义序列
* woff字体的解析
