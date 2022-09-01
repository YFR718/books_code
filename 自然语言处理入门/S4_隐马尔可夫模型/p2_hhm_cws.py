# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-19 14:33
# 《自然语言处理入门》4.6 隐马尔可夫模型应用于中文分词
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *

from 自然语言处理入门.S3_二元语法与中文分词.p0_msr import msr_test, msr_output, msr_gold, msr_dict, msr_train
from 自然语言处理入门.S3_二元语法与中文分词.p5_eval_bigram_cws import CWSEvaluator

FirstOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.FirstOrderHiddenMarkovModel')
SecondOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.SecondOrderHiddenMarkovModel')
HMMSegmenter = JClass('com.hankcs.hanlp.model.hmm.HMMSegmenter')


def train(corpus, model):
    segmenter = HMMSegmenter(model)
    segmenter.train(corpus)
    print(segmenter.segment('商品和服务'))
    return segmenter.toSegment()


def evaluate(segment):
    result = CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict)
    print(result)


if __name__ == '__main__':
    segment = train(msr_train, FirstOrderHiddenMarkovModel())
    evaluate(segment)
    segment = train(msr_train, SecondOrderHiddenMarkovModel())
    evaluate(segment)
