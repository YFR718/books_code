# -*- coding:utf-8 -*-
# 《自然语言处理入门》9.2 关键词提取

from pyhanlp import *

TfIdfCounter = JClass('com.hankcs.hanlp.mining.word.TfIdfCounter')




if __name__ == '__main__':
    counter = TfIdfCounter()
    with open(r'C:\Users\24378\Downloads\斗破苍穹.txt', encoding='utf-8') as src:
        i = 0
        caption = ""
        texts = []
        for line in src.readlines():
            if line != '\n':
                if line[1] == "第":
                    if caption != "":
                        counter.add(caption,",".join(texts))
                    caption = line.strip()
                    texts = []
                    i += 1
                    if i > 100:
                        break
                else:
                    texts.append(line.strip())

    counter.add("《女排夺冠》", "女排北京奥运会夺冠")  # 输入多篇文档
    counter.add("《羽毛球男单》", "北京奥运会的羽毛球男单决赛")
    counter.add("《女排》", "中国队女排夺北京奥运会金牌重返巅峰，观众欢呼女排女排女排！")
    counter.compute()  # 输入完毕
    i = 0
    for id in counter.documents():
        print(id + " : " + counter.getKeywordsOf(id, 20).toString())  # 根据每篇文档的TF-IDF提取关键词

    # 根据语料库已有的IDF信息为语料库之外的新文档提取关键词
    print(counter.getKeywords("奥运会反兴奋剂", 2))
