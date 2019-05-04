#coding:utf-8

from util import dec
from commons import decrypt_tags
from bs4.element import Tag

def decrypt_woff_tag(tag,TTGlyphs,d_list):
    contents = tag.contents
    _ = []
    while contents:
        i = contents.pop(0)
        if isinstance(i, Tag):
            if i.name in decrypt_tags:
                text = dec(i.text)
                for index,name in enumerate(TTGlyphs):
                    if text in name:
                        i = d_list[index]  
            else:
                continue
        elif not isinstance(i, str):
            continue
        _.append(i)
    return ''.join(_)
