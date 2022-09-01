# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-05 15:12
# 《自然语言处理入门》7.3.1 基于隐马尔可夫模型的词性标注
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *

from 自然语言处理入门.S7_词性标注.p1_pku import PKU199801_TRAIN, PKU199801_TEST
from 自然语言处理入门.S7_词性标注.p2_demo_hmm_pos import train_hmm_pos, FirstOrderHiddenMarkovModel, \
    SecondOrderHiddenMarkovModel
from 自然语言处理入门.S7_词性标注.p3_demo_perceptron_pos import train_perceptron_pos
from 自然语言处理入门.S7_词性标注.p4_demo_crf_pos import train_crf_pos

PosTagUtil = JClass('com.hankcs.hanlp.dependency.nnparser.util.PosTagUtil')

print("一阶HMM\t%.2f%%" % (
    PosTagUtil.evaluate(train_hmm_pos(PKU199801_TRAIN, FirstOrderHiddenMarkovModel()), PKU199801_TEST)))
print("二阶HMM\t%.2f%%" % (
    PosTagUtil.evaluate(train_hmm_pos(PKU199801_TRAIN, SecondOrderHiddenMarkovModel()), PKU199801_TEST)))
print("感知机\t%.2f%%" % (PosTagUtil.evaluate(train_perceptron_pos(PKU199801_TRAIN), PKU199801_TEST)))
print("CRF\t%.2f%%" % (PosTagUtil.evaluate(train_crf_pos(PKU199801_TRAIN), PKU199801_TEST)))
