# -*- coding:utf-8 -*-
# 《自然语言处理入门》8.5.3 基于感知机序列标注的命名实体识别

from pyhanlp import *

from 自然语言处理入门.S7_词性标注.p1_pku import PKU199801_TRAIN, NER_MODEL
from 自然语言处理入门.S8_命名实体识别.p2_demo_role_tag_nr import Sentence
from 自然语言处理入门.S8_命名实体识别.p5_demo_hmm_ner import PerceptronSegmenter, PerceptronPOSTagger
from 自然语言处理入门.S8_命名实体识别.p5_demo_hmm_ner import test
NERTrainer = JClass('com.hankcs.hanlp.model.perceptron.NERTrainer')
PerceptronNERecognizer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronNERecognizer')


def train(corpus, model):
    trainer = NERTrainer()
    return PerceptronNERecognizer(trainer.train(corpus, model).getModel())


if __name__ == '__main__':
    recognizer = train(PKU199801_TRAIN, NER_MODEL)
    test(recognizer)
    analyzer = PerceptronLexicalAnalyzer(PerceptronSegmenter(), PerceptronPOSTagger(), recognizer)  # ①
    sentence = Sentence.create("与/c 特朗普/nr 通/v 电话/n 讨论/v [太空/s 探索/vn 技术/n 公司/n]/nt")  # ②
    while not analyzer.analyze(sentence.text()).equals(sentence):  # ③
        analyzer.learn(sentence)
