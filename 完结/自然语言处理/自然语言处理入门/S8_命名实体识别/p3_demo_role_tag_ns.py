# -*- coding:utf-8 -*-
# 《自然语言处理入门》8.4.2 基于角色标注的地名识别

from pyhanlp import *

from 自然语言处理入门.S3_二元语法与中文分词.p3_ngram_segment import DijkstraSegment
from 自然语言处理入门.S7_词性标注.p1_pku import PKU199801
from 自然语言处理入门.S8_命名实体识别.p2_demo_role_tag_nr import EasyDictionary
from 自然语言处理入门.tools.test_utility import test_data_path


NSDictionaryMaker = JClass('com.hankcs.hanlp.corpus.dictionary.NSDictionaryMaker')

MODEL = test_data_path() + "/ns"


def train(corpus, model):
    dictionary = EasyDictionary.create(HanLP.Config.CoreDictionaryPath)  # 核心词典
    maker = NSDictionaryMaker(dictionary)  # 训练模块
    maker.train(corpus)  # 在语料库上训练
    maker.saveTxtTo(model)  # 输出HMM到txt


def load(model):
    HanLP.Config.PlaceDictionaryPath = model + ".txt"  # data/test/ns.txt
    HanLP.Config.PlaceDictionaryTrPath = model + ".tr.txt"  # data/test/ns.tr.txt
    segment = DijkstraSegment().enablePlaceRecognize(True).enableCustomDictionary(False)  # 该分词器便于调试
    return segment


def test(model=MODEL):
    segment = load(model)
    HanLP.Config.enableDebug()
    print(segment.seg("生于黑牛沟村"))


if __name__ == '__main__':
    train(PKU199801, MODEL)
    test(MODEL)
