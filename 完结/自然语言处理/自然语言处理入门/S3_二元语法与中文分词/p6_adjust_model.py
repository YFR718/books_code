# -*- coding:utf-8 -*-
# 《自然语言处理入门》3.5.3 调整模型
import os
from pyhanlp import HanLP

from 自然语言处理入门.S3_二元语法与中文分词.p0_msr import msr_model
from 自然语言处理入门.S3_二元语法与中文分词.p3_ngram_segment import load_bigram, CoreDictionary

from 自然语言处理入门.tools.test_utility import test_data_path


segment = load_bigram(model_path=msr_model, verbose=False, ret_viterbi=False)
assert CoreDictionary.contains("管道")
text = "北京输气管道工程"
HanLP.Config.enableDebug()
print(segment.seg(text))