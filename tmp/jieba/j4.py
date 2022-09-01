import jieba
import jieba.posseg as pseg


words = pseg.cut('自然语言处理是人工智能的子领域')
for word, flag in words:
    print('{} {}'.format(word, flag))