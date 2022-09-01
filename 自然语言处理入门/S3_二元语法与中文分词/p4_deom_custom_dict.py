# -*- coding:utf-8 -*-
# 《自然语言处理入门》3.4.5 与用户词典的集成
from pyhanlp import *

from 自然语言处理入门.S3_二元语法与中文分词.p3_ngram_segment import ViterbiSegment

segment = ViterbiSegment()
sentence = "社会摇摆简称社会摇"
segment.enableCustomDictionary(False)
print("不挂载词典：", segment.seg(sentence))
CustomDictionary.insert("社会摇", "nz 100")
segment.enableCustomDictionary(True)
print("低优先级词典：", segment.seg(sentence))
segment.enableCustomDictionaryForcing(True)
print("高优先级词典：", segment.seg(sentence))
