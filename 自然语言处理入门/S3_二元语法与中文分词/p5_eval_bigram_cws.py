# -*- coding:utf-8 -*-
# 《自然语言处理入门》3.5.1 标准化评测

from pyhanlp import *

from 自然语言处理入门.S3_二元语法与中文分词.p0_msr import msr_train, msr_test, msr_output, msr_gold, msr_dict
from 自然语言处理入门.S3_二元语法与中文分词.p3_ngram_segment import train_bigram, load_bigram, msr_model


CWSEvaluator = SafeJClass('com.hankcs.hanlp.seg.common.CWSEvaluator')

if __name__ == '__main__':
    train_bigram(msr_train, msr_model)  # 训练
    segment = load_bigram(msr_model,verbose=False)  # 加载
    result = CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict)  # 预测打分
    print(result)

# P:92.62 R:96.85 F1:94.69 OOV-R:2.58 IV-R:99.41