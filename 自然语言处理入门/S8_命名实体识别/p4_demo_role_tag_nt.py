# -*- coding:utf-8 -*-
# 《自然语言处理入门》8.4.3 基于角色标注的机构名识别

from pyhanlp import *

from 自然语言处理入门.S3_二元语法与中文分词.p3_ngram_segment import DijkstraSegment
from 自然语言处理入门.S7_词性标注.p1_pku import PKU199801
from 自然语言处理入门.S8_命名实体识别.p2_demo_role_tag_nr import EasyDictionary
from 自然语言处理入门.tools.test_utility import test_data_path


NTDictionaryMaker = JClass('com.hankcs.hanlp.corpus.dictionary.NTDictionaryMaker')

MODEL = test_data_path() + "/ns"


def train(corpus, model):
    dictionary = EasyDictionary.create(HanLP.Config.CoreDictionaryPath)  # 核心词典
    maker = NTDictionaryMaker(dictionary)  # 训练模块
    maker.train(corpus)  # 在语料库上训练
    maker.saveTxtTo(model)  # 输出HMM到txt


def load(model):
    HanLP.Config.PlaceDictionaryPath = model + ".txt"  # data/test/ns.txt
    HanLP.Config.PlaceDictionaryTrPath = model + ".tr.txt"  # data/test/ns.tr.txt
    segment = DijkstraSegment().enableOrganizationRecognize(True).enableCustomDictionary(False)  # 该分词器便于调试
    return segment


def test(model=MODEL):
    segment = load(model)
    HanLP.Config.enableDebug()
    print(segment.seg("温州黄鹤皮革制造有限公司是由黄先生创办的企业"))


if __name__ == '__main__':
    train(PKU199801, MODEL)
    test(MODEL)
