# -*- coding:utf-8 -*-
# 《自然语言处理入门》5.6 基于结构化感知机的中文分词


from pyhanlp import *

from 自然语言处理入门.S3_二元语法与中文分词.p0_msr import msr_train, msr_model, msr_test, msr_output, msr_gold, msr_dict
from 自然语言处理入门.S5_感知机分类与序列标注.p4_percetron_cws import CWSTrainer

PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
LinearModel = JClass('com.hankcs.hanlp.model.perceptron.model.LinearModel')
Segment = JClass('com.hankcs.hanlp.seg.Segment')
CWSEvaluator = JClass('com.hankcs.hanlp.seg.common.CWSEvaluator')


def trainStructuredPerceptron():
    model = CWSTrainer().train(msr_train, msr_train, msr_model, 0., 10, 8).getModel()
    return PerceptronLexicalAnalyzer(model).enableCustomDictionary(False)


def trainAveragedPerceptron():
    model = CWSTrainer().train(msr_train, msr_train, msr_model, 0., 10, 1).getModel()
    return PerceptronLexicalAnalyzer(model).enableCustomDictionary(False)


print("结构化感知机")
print(CWSEvaluator.evaluate(trainStructuredPerceptron(), msr_test, msr_output, msr_gold, msr_dict))
print("平均感知机")
print(CWSEvaluator.evaluate(trainAveragedPerceptron(), msr_test, msr_output, msr_gold, msr_dict))
