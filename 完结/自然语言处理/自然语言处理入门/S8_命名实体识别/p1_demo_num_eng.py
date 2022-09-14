# -*- coding:utf-8 -*-
# 《自然语言处理入门》8.2.3 基于规则的数词英文识别

from pyhanlp import *

from 自然语言处理入门.S3_二元语法与中文分词.p3_ngram_segment import ViterbiSegment

CharType = JClass('com.hankcs.hanlp.dictionary.other.CharType')

segment = ViterbiSegment()
print(segment.seg("牛奶三〇〇克壹佰块"))
print(segment.seg("牛奶300克100块"))
print(segment.seg("牛奶300g100rmb"))
# 演示自定义字符类型
text = "牛奶300~400g100rmb"
print(segment.seg(text))
CharType.set('~', CharType.CT_NUM)
print(segment.seg(text))
