import jieba

seg_list = jieba.cut('自然语言处理是人工智能的子领域')
print('没有自定义词典：{}'.format('\ '.join(seg_list)))

jieba.load_userdict('./userdict.txt')
seg_list = jieba.cut('自然语言处理是人工智能的子领域')
print('有自定义词典：{}'.format('\ '.join(seg_list)))