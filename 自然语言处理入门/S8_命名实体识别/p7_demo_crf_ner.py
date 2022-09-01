# -*- coding:utf-8 -*-
# 《自然语言处理入门》8.5.4 基于条件随机场序列标注的命名 实体识别

from pyhanlp import *

from 自然语言处理入门.S7_词性标注.p1_pku import PKU199801_TRAIN, NER_MODEL
from 自然语言处理入门.S8_命名实体识别.p5_demo_hmm_ner import test


CRFNERecognizer = JClass('com.hankcs.hanlp.model.crf.CRFNERecognizer')


def train(corpus, model):
    recognizer = CRFNERecognizer(None)  # 空白
    recognizer.train(corpus, model)
    return recognizer


if __name__ == '__main__':
    recognizer = train(PKU199801_TRAIN, NER_MODEL)
    test(recognizer)
