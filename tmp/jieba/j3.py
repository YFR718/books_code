import jieba

jieba.add_word('自然语言处理')
jieba.suggest_freq(('人工', '智能'), tune=True)
jieba.suggest_freq('子领域', tune=True)

seg_list = jieba.cut('自然语言处理是人工智能的子领域')
print('\ '.join(seg_list))