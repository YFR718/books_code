# -*- coding:utf-8 -*-
# 《自然语言处理入门》2.2.2 词典的加载

from pyhanlp import *


def load_dictionary():
    """
    加载HanLP中的mini词库
    :return: 一个set形式的词库
    """
    # use ioutil
    IOUtil = JClass('com.hankcs.hanlp.corpus.io.IOUtil')
    # config dictionary path
    # path = HanLP.Config.CoreDictionaryPath.replace('.txt', '.mini.txt')
    path = HanLP.Config.CoreDictionaryPath.replace('.txt', '.txt')
    # load dictionary
    dic = IOUtil.loadDictionary([path])
    return set(dic.keySet())


if __name__ == '__main__':
    dic = load_dictionary()
    print(len(dic))
    print(list(dic)[0])
