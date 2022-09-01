import jieba

sentence = '南京市长江大桥'

seg_list = jieba.cut(sentence, cut_all=True)
print('全模式：{}'.format('/ '.join(seg_list)))

seg_list = jieba.cut(sentence, cut_all=False)
print('精准模式：{}'.format('/ '.join(seg_list)))

seg_list = jieba.cut_for_search(sentence,HMM=True)
print('搜索引擎模式：{}'.format('/ '.join(seg_list)))
seg_list = jieba.cut_for_search(sentence,HMM=False)
print('搜索引擎模式：{}'.format('/ '.join(seg_list)))