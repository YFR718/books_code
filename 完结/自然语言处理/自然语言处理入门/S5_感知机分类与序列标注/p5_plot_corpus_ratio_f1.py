# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-22 17:53
# 《自然语言处理入门》5.6.3 特征裁剪与模型压缩
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from tempfile import NamedTemporaryFile

import numpy as np

__doc__ = '试验语料库规模对准确率的影响'


import matplotlib.pyplot as plt
from pyhanlp import PerceptronLexicalAnalyzer

from 自然语言处理入门.S3_二元语法与中文分词.p0_msr import msr_train, msr_test, msr_output, msr_dict, msr_gold
from 自然语言处理入门.S3_二元语法与中文分词.p3_ngram_segment import msr_model
from 自然语言处理入门.S3_二元语法与中文分词.p5_eval_bigram_cws import  CWSEvaluator
from 自然语言处理入门.S5_感知机分类与序列标注.p4_percetron_cws import CWSTrainer

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def train_evaluate(ratio):
    partial_corpus = NamedTemporaryFile(delete=False).name
    with open(msr_train,encoding="utf-8") as src, open(partial_corpus, 'w',encoding="utf-8") as dst:
        all_lines = src.readlines()
        dst.writelines(all_lines[:int(ratio * len(all_lines))])

    model = CWSTrainer().train(partial_corpus, partial_corpus, msr_model, 0, 50, 8).getModel()  # 训练模型
    result = CWSEvaluator.evaluate(PerceptronLexicalAnalyzer(model).enableCustomDictionary(False),
                                   msr_test, msr_output, msr_gold, msr_dict)
    return result.F1


if __name__ == '__main__':
    x = [r / 10 for r in range(1, 11)]
    y = [train_evaluate(r) for r in x]
    plt.title("语料库规模对准确率的影响")
    plt.xlabel("语料库规模（万字符）")
    plt.ylabel("准确率")
    plt.xticks([int(r / 10 * 405) for r in range(1, 11)])
    plt.yticks(np.arange(91, 97.5, 0.5))
    plt.plot([int(r / 10 * 405) for r in range(1, 11)], y, color='b')
    plt.grid()
    plt.show()
