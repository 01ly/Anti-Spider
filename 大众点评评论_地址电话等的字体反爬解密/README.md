# 大众点评 字体反爬

## 实时更新：
 2. **2019-10-30** （现版本） :
>  > * 获取 店铺首页需要增加请求头部增加 cookie 的 **_lxsdk_cuid**值
>  > * 更新解密woff字体顺序，实现最新电话地址评论内容解密
>  > * cookie中的 **_lxsdk_cuid** 具有时效性，请根据自身情况更换



 1. **2019-05-04** (已废弃):
>  * 访问的店铺url示例：
>  > * (url-a) http://www.dianping.com/shop/2832061
>  > * (url-b) http://www.dianping.com/shop/15960860/review_all
>  * 更新内容:
>  > * 针对url-a 的访问页面进行 **地址**、**电话** 的woff字体反爬解密
>  > * 针对url-a 的访问页面进行 **点评评论** 的woff字体反爬解密
>  > * 针对url-b 的访问页面进行 **地址**、**电话**的svg反爬解密(详见github库: [01ly/DPSpider](https://github.com/01ly/DPspider))
>  > * 针对url-b 的访问页面进行 **点评评论** 的woff字体反爬解密(与url-a的解密一致)

# **changelog**

##1.示例(2019年10月31日版 web大众点评)

在当前路径下打开DOS:
* 解密当前woff字体显示的加密评论：
` python comment_decrypt.py`
* 解密当前woff字体显示的加密电话、地址：
` python addr_phone_decrypt.py`
* 测试解密电话、地址、评论:
` python test.py`

##0.示例(2019年5月4日版 web大众点评)

* 解密当前woff字体显示的加密评论：
` python url-a-comment-decrypt.py`
* 解密当前woff字体显示的加密电话、地址：
` python url-a-addr-phone-decrypt.py`

## 反爬点

* 使用woff字体前端显示 出现html 的NCR转义序列
* woff字体的解析

## 交流讨论

微信公众号:
![gzh](../qrcode.jpg)
qq群：
![qq](../qq.png)

## 捐献

**If this repo helps,maybe you can buy me a cup of coffee :)**

支付宝：
![](../alipay.jpg)
微信：
![](../wechat.png)
