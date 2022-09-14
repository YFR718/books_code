# -*- coding:utf-8 -*-
# 《自然语言处理入门》7.3.2 基于感知机的词性标注


from pyhanlp import *

from 自然语言处理入门.S7_词性标注.p1_pku import POS_MODEL, PKU199801_TRAIN
from 自然语言处理入门.S7_词性标注.p2_demo_hmm_pos import AbstractLexicalAnalyzer, PerceptronSegmenter
from 自然语言处理入门.S8_命名实体识别.p5_demo_hmm_ner import PerceptronPOSTagger

POSTrainer = JClass('com.hankcs.hanlp.model.perceptron.POSTrainer')


def train_perceptron_pos(corpus):
    trainer = POSTrainer()
    trainer.train(corpus, POS_MODEL)  # 训练
    tagger = PerceptronPOSTagger(POS_MODEL)  # 加载
    print(', '.join(tagger.tag("他", "的", "希望", "是", "希望", "上学")))  # 预测
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), tagger)  # 构造词法分析器
    print(analyzer.analyze("李狗蛋的希望是希望上学"))  # 分词+词性标注
    return tagger


if __name__ == '__main__':
    train_perceptron_pos(PKU199801_TRAIN)
