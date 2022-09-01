# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-02 14:43
# 《自然语言处理入门》6.4 HanLP 中的 CRF++ API
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

from pyhanlp import *

from 自然语言处理入门.S3_二元语法与中文分词.p0_msr import msr_train, msr_test, msr_output, msr_gold, msr_dict
from 自然语言处理入门.S5_感知机分类与序列标注.p8_eval_perceptron_cws import CWSEvaluator

from 自然语言处理入门.S6_条件随机场与序列标注.p3_crfpp_train_hanlp_load import CRF_MODEL_PATH

CRFSegmenter = JClass('com.hankcs.hanlp.model.crf.CRFSegmenter')
CRFLexicalAnalyzer = JClass('com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer')


def train(corpus):
    segmenter = CRFSegmenter(None)
    segmenter.train(corpus, CRF_MODEL_PATH)
    return CRFLexicalAnalyzer(segmenter)
    # 训练完毕时，可传入txt格式的模型（不可传入CRF++的二进制模型，不兼容！）
    # return CRFLexicalAnalyzer(CRF_MODEL_TXT_PATH).enableCustomDictionary(False)


if __name__ == '__main__':
    segment = train(msr_train)
    print(CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict))  # 标准化评测
