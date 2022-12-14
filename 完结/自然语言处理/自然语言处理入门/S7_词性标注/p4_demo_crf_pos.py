# -*- coding:utf-8 -*-
# 《自然语言处理入门》7.3.3 基于条件随机场的词性标注

from pyhanlp import *

from 自然语言处理入门.S7_词性标注.p1_pku import POS_MODEL, PKU199801_TRAIN
from 自然语言处理入门.S7_词性标注.p2_demo_hmm_pos import AbstractLexicalAnalyzer, PerceptronSegmenter

CRFPOSTagger = JClass('com.hankcs.hanlp.model.crf.CRFPOSTagger')


def train_crf_pos(corpus):
    # 选项1.使用HanLP的Java API训练，慢
    tagger = CRFPOSTagger(None)  # 创建空白标注器
    tagger.train(corpus, POS_MODEL)  # 训练
    tagger = CRFPOSTagger(POS_MODEL) # 加载
    # 选项2.使用CRF++训练，HanLP加载。（训练命令由选项1给出）
    # tagger = CRFPOSTagger(POS_MODEL + ".txt")
    print(', '.join(tagger.tag("他", "的", "希望", "是", "希望", "上学")))  # 预测
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), tagger)  # 构造词法分析器
    print(analyzer.analyze("李狗蛋的希望是希望上学"))  # 分词+词性标注
    return tagger



if __name__ == '__main__':
    tagger = train_crf_pos(PKU199801_TRAIN)
