# -*- coding:utf-8 -*-
# 《自然语言处理入门》6.4 HanLP 中的 CRF++ API

from pyhanlp import *

from 自然语言处理入门.S3_二元语法与中文分词.p2_corpus_loader import my_cws_corpus
from 自然语言处理入门.tools.test_utility import test_data_path

CRFLexicalAnalyzer = JClass('com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer')

TXT_CORPUS_PATH = my_cws_corpus()
TSV_CORPUS_PATH = TXT_CORPUS_PATH + ".tsv"
TEMPLATE_PATH = test_data_path() + "/cws-template.txt"
CRF_MODEL_PATH = test_data_path() + "/crf-cws-model"
CRF_MODEL_TXT_PATH = test_data_path() + "/crf-cws-model.txt"


def train_or_load(corpus_txt_path=TXT_CORPUS_PATH, model_txt_path=CRF_MODEL_TXT_PATH):
    print(model_txt_path)
    if os.path.isfile(model_txt_path):  # 已训练，直接加载
        segmenter = CRFLexicalAnalyzer(model_txt_path)
        return segmenter
    else:
        segmenter = CRFLexicalAnalyzer(None)  # 创建空白分词器
        segmenter.convertCorpus(corpus_txt_path, TSV_CORPUS_PATH)  # 执行转换
        segmenter.dumpTemplate(TEMPLATE_PATH)  # 导出特征模板
        # 交给CRF++训练
        print("语料已转换为 %s ，特征模板已导出为 %s" % (TSV_CORPUS_PATH, TEMPLATE_PATH))
        print("请安装CRF++后执行 crf_learn -f 3 -c 4.0 %s %s %s -t" % (TEMPLATE_PATH, TSV_CORPUS_PATH, CRF_MODEL_PATH))
        print("或者执行移植版 java -cp hanlp.jar com.hankcs.hanlp.model.crf.crfpp.crf_learn -f 3 -c 4.0 %s %s %s -t" % (
            TEMPLATE_PATH, TSV_CORPUS_PATH, CRF_MODEL_PATH))


if __name__ == '__main__':
    segment = train_or_load()
    print(segment.segment("商品和服务"))
