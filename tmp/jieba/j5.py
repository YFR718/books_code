import re

re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&\._%]+)", re.U)
re_han_cut_all = re.compile("([\u4E00-\u9FD5]+)", re.U)

sentence = "好好学习good good study，天天向上day day up。"

blocks = re_han_default.split(sentence)
print("精准模式re_han_default的切分结果：")
print(blocks)

print()

blocks = re_han_cut_all.split(sentence)
print("全模式re_han_cut_all的切分结果：")
print(blocks)