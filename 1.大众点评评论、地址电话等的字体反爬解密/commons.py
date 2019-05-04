#coding:utf-8

schema = 'https://'

decrypt_tags = ['svgmtsi','d','e']

woff_a_path_name = 'woff/url-a.woff'
woff_b_path_name = 'woff/url-b.woff'

woff_a_to_xml = 'xml/url-a.xml'
woff_b_to_xml = 'xml/url-b.xml'

pattern_svgcss = r'//(s3plus.meituan.net.+?)"'
pattern_woff = r'url\("//(.+?)"'

example_shop_url_a = 'https://www.dianping.com/shop/15960860'
example_shop_url_b = 'https://www.dianping.com/shop/15960860/review_all'

example_shop_html_a = 'example_html/shop0.html'
example_shop_html_b = 'example_html/shop1.html'

comment_tag_finder = {
    'url-a':('ul',{'id':'reviewlist-wrapper'}),
    'url-a-li':('li',{'class_':'comment-item'}),
    'url-a-p':('p',{'class_':'desc J-desc'}),
    'url-a-address':('span',{'id':'address'}),
    'url-a-phone':('p',{'class_':'expand-info tel'})
}

request_headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Host':'www.dianping.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
