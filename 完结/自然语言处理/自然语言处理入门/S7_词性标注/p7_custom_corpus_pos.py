# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-06 13:54
# 《自然语言处理入门》7.4.2 标注语料
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from 自然语言处理入门.S7_词性标注.p2_demo_hmm_pos import AbstractLexicalAnalyzer, PerceptronSegmenter
from 自然语言处理入门.S7_词性标注.p3_demo_perceptron_pos import train_perceptron_pos
from 自然语言处理入门.tools.test_utility import ensure_data

ZHUXIAN = ensure_data("zhuxian", "http://file.hankcs.com/corpus/zhuxian.zip") + "/train.txt"
posTagger = train_perceptron_pos(ZHUXIAN)  # 训练
analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), posTagger)  # 包装
print(analyzer.analyze("陆雪琪的天琊神剑不做丝毫退避，直冲而上，瞬间，这两道奇光异宝撞到了一起。"))  # 分词+标注
