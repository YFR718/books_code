# -*- coding:utf-8 -*-

# 《自然语言处理入门》3.6.1 日语分词语料

import os

from 自然语言处理入门.S3_二元语法与中文分词.p3_ngram_segment import  train_bigram, load_bigram
from 自然语言处理入门.tools.test_utility import ensure_data

jp_corpus = ensure_data('jpcorpus','http://file.hankcs.com/corpus/jpcorpus.zip')
jp_bigram = os.path.join(jp_corpus, 'jp_bigram')
jp_corpus = os.path.join(jp_corpus, 'ja_gsd-ud-train.txt')

if __name__ == '__main__':
    train_bigram(jp_corpus, jp_bigram)  # 训练
    segment = load_bigram(jp_bigram, verbose=False)  # 加载
    print(segment.seg('自然言語処理入門という本が面白いぞ！'))  # 日语分词
