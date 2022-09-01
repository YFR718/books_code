from jpype import JClass

from 自然语言处理入门.S2_词典分词.p2_utility import load_dictionary
from 自然语言处理入门.S2_词典分词.p3_sample_segment import evaluate_speed, forwardSegment


class Node(object):
    def __init__(self, value) -> None:
        self._children = {}  # store char to child nodes
        self._value = value  # store the signal of the node

    def _add_child(self, char, value, overwrite=False):
        child = self._children.get(char)
        if child is None:
            child = Node(value)
            self._children[char] = child
        elif overwrite:
            child._value = value
        return child


class Trie(Node):
    def __init__(self) -> None:
        super().__init__(None)

    def __contains__(self, key):
        return self[key] is not None

    def __getitem__(self, key):
        state = self
        for char in key:
            state = state._children.get(char)
            if state is None:
                return None
        return state._value

    def __setitem__(self, key, value):
        state = self
        for i, char in enumerate(key):
            if i < len(key) - 1:
                state = state._add_child(char, None, False)
            else:
                state = state._add_child(char, value, True)


def forwardSegment_prefix_speedup(s: str, dic):
    ans = []
    l = 0
    while l < len(s):
        longest_word = ""
        for r in range(l + 1, len(s)):
            word = str(s[l:r])
            # find the longest word
            if word in dic:
                longest_word = word
            else:
                break
        if len(longest_word) > 0:
            ans.append(longest_word)
            l += len(longest_word)
        else:
            l += 1
    return ans

class DoubleArrayTrie(object):
    def __init__(self, dic: dict) -> None:
        m = JClass('java.util.TreeMap')()
        for k, v in dic.items():
            m[k] = v
        DoubleArrayTrie = JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')
        dat = DoubleArrayTrie(m)
        self.base = dat.getBase()
        self.check = dat.getCheck()
        self.value = dat.getValueArray([''])

    @staticmethod
    def char_hash(c) -> int:
        return JClass('java.lang.Character')(c).hashCode()

    def transition(self, c, b) -> int:
        """
        状态转移
        :param c: 字符
        :param b: 初始状态
        :return: 转移后的状态，-1表示失败
        """
        p = self.base[b] + self.char_hash(c) + 1
        if self.base[b] == self.check[p]:
            return p
        else:
            return -1

    def __getitem__(self, key: str):
        b = 0
        print(key)
        print(type(key))
        for i in range(0, len(key)):  # len(key)次状态转移
            p = self.transition(key[i], b)
            if p != -1:
                b = p
            else:
                return None

        p = self.base[b]  # 按字符'\0'进行状态转移
        n = self.base[p]  # 查询base
        if p == self.check[p] and n < 0:  # 状态转移成功且对应词语结尾
            index = -n - 1  # 取得字典序
            return self.value[index]
        return None

if __name__ == '__main__':
    trie = Trie()

    dic = load_dictionary()
    for k in dic:
        trie[k] = 1

    dd = {}
    for d in dic:
        dd[d] = 1
    dtrie = DoubleArrayTrie(dd)

    text10 = "江西鄱阳湖干枯，中国"
    text100 = "我们一般认为，抓住了问题的关键，其他一切则会迎刃而解。 既然如此， 在这种困难的抉择下，本人思来想去，寝食难安。 笛卡儿曾经提到过，读一切好书，就是和许多高尚的人谈话。我希望诸位也能好好地体会这句话。"
    text1000 = "每个人都不得不面对这些问题。 在面对这种问题时， 而这些并不是完全重要，更加重要的问题是。我认为， 叔本华说过一句著名的话，意志是一个强壮的盲人，倚靠在明眼的跛子肩上。这句话语虽然很短, " \
               "但令我浮想联翩. 了解清楚问题到底是一种怎么样的存在，是解决一切问题的关键。 而这些并不是完全重要，更加重要的问题是， 问题的发生，到底需要如何做到，不问题的发生，又会如何产生。 " \
               "带着这些问题，我们来审视一下问题。 问题，到底应该如何实现。 对我个人而言，问题不仅仅是一个重大的事件，还可能会改变我的人生。 这样看来， 要想清楚，问题，到底是一种怎么样的存在。 " \
               "所谓问题，关键是问题需要如何写。 所谓问题，关键是问题需要如何写。 在这种困难的抉择下，本人思来想去，寝食难安。 经过上述讨论， 我们都知道，只要有意义，那么就必须慎重考虑。 " \
               "本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。 就我个人来说，问题对我的意义，不能不说非常重大。 现在，解决问题的问题，是非常非常重要的。 所以， 问题的关键究竟为何？ " \
               "问题的发生，到底需要如何做到，不问题的发生，又会如何产生。 我们都知道，只要有意义，那么就必须慎重考虑。 我们都知道，只要有意义，那么就必须慎重考虑。 问题，到底应该如何实现。 " \
               "这种事实对本人来说意义重大，相信对这个世界也是有一定意义的。 既然如何， 歌德曾经说过，决定一个人的一生，以及整个命运的，只是一瞬之间。这启发了我. 每个人都不得不面对这些问题。 在面对这种问题时， " \
               "问题，发生了会如何，不发生又会如何。 既然如何， 问题的关键究竟为何？ 这种事实对本人来说意义重大，相信对这个世界也是有一定意义的。 那么， 生活中，若问题出现了，我们就不得不考虑它出现了的事实。 " \
               "既然如何， 可是，即使是这样，问题的出现仍然代表了一定的意义。 塞内加说过一句富有哲理的话，勇气通往天堂，怯懦通往地狱。这句话把我们带到了一个新的维度去思考这个问题: " \
               "希腊说过一句富有哲理的话，最困难的事情就是认识自己。这句话把我们带到了一个新的维度去思考这个问题: 我认为， 问题，到底应该如何实现。 所谓问题，关键是问题需要如何写。 " \
               "本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。 一般来说， 每个人都不得不面对这些问题。 在面对这种问题时， 黑格尔说过一句著名的话，只有永远躺在泥坑里的人，才不会再掉进坑里。这句话语虽然很短, " \
               "但令我浮想联翩。 "
    text2000 = "每个人都不得不面对这些问题。 在面对这种问题时， 而这些并不是完全重要，更加重要的问题是。我认为， 叔本华说过一句著名的话，意志是一个强壮的盲人，倚靠在明眼的跛子肩上。这句话语虽然很短, " \
               "但令我浮想联翩. 了解清楚问题到底是一种怎么样的存在，是解决一切问题的关键。 而这些并不是完全重要，更加重要的问题是， 问题的发生，到底需要如何做到，不问题的发生，又会如何产生。 " \
               "带着这些问题，我们来审视一下问题。 问题，到底应该如何实现。 对我个人而言，问题不仅仅是一个重大的事件，还可能会改变我的人生。 这样看来， 要想清楚，问题，到底是一种怎么样的存在。 " \
               "所谓问题，关键是问题需要如何写。 所谓问题，关键是问题需要如何写。 在这种困难的抉择下，本人思来想去，寝食难安。 经过上述讨论， 我们都知道，只要有意义，那么就必须慎重考虑。 " \
               "本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。 就我个人来说，问题对我的意义，不能不说非常重大。 现在，解决问题的问题，是非常非常重要的。 所以， 问题的关键究竟为何？ " \
               "问题的发生，到底需要如何做到，不问题的发生，又会如何产生。 我们都知道，只要有意义，那么就必须慎重考虑。 我们都知道，只要有意义，那么就必须慎重考虑。 问题，到底应该如何实现。 " \
               "这种事实对本人来说意义重大，相信对这个世界也是有一定意义的。 既然如何， 歌德曾经说过，决定一个人的一生，以及整个命运的，只是一瞬之间。这启发了我. 每个人都不得不面对这些问题。 在面对这种问题时， " \
               "问题，发生了会如何，不发生又会如何。 既然如何， 问题的关键究竟为何？ 这种事实对本人来说意义重大，相信对这个世界也是有一定意义的。 那么， 生活中，若问题出现了，我们就不得不考虑它出现了的事实。 " \
               "既然如何， 可是，即使是这样，问题的出现仍然代表了一定的意义。 塞内加说过一句富有哲理的话，勇气通往天堂，怯懦通往地狱。这句话把我们带到了一个新的维度去思考这个问题: " \
               "希腊说过一句富有哲理的话，最困难的事情就是认识自己。这句话把我们带到了一个新的维度去思考这个问题: 我认为， 问题，到底应该如何实现。 所谓问题，关键是问题需要如何写。 " \
               "本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。 一般来说， 每个人都不得不面对这些问题。 在面对这种问题时， 黑格尔说过一句著名的话，只有永远躺在泥坑里的人，才不会再掉进坑里。这句话语虽然很短, " \
               "但令我浮想联翩。 " \
               "每个人都不得不面对这些问题。 在面对这种问题时， 而这些并不是完全重要，更加重要的问题是。我认为， 叔本华说过一句著名的话，意志是一个强壮的盲人，倚靠在明眼的跛子肩上。这句话语虽然很短, " \
               "但令我浮想联翩. 了解清楚问题到底是一种怎么样的存在，是解决一切问题的关键。 而这些并不是完全重要，更加重要的问题是， 问题的发生，到底需要如何做到，不问题的发生，又会如何产生。 " \
               "带着这些问题，我们来审视一下问题。 问题，到底应该如何实现。 对我个人而言，问题不仅仅是一个重大的事件，还可能会改变我的人生。 这样看来， 要想清楚，问题，到底是一种怎么样的存在。 " \
               "所谓问题，关键是问题需要如何写。 所谓问题，关键是问题需要如何写。 在这种困难的抉择下，本人思来想去，寝食难安。 经过上述讨论， 我们都知道，只要有意义，那么就必须慎重考虑。 " \
               "本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。 就我个人来说，问题对我的意义，不能不说非常重大。 现在，解决问题的问题，是非常非常重要的。 所以， 问题的关键究竟为何？ " \
               "问题的发生，到底需要如何做到，不问题的发生，又会如何产生。 我们都知道，只要有意义，那么就必须慎重考虑。 我们都知道，只要有意义，那么就必须慎重考虑。 问题，到底应该如何实现。 " \
               "这种事实对本人来说意义重大，相信对这个世界也是有一定意义的。 既然如何， 歌德曾经说过，决定一个人的一生，以及整个命运的，只是一瞬之间。这启发了我. 每个人都不得不面对这些问题。 在面对这种问题时， " \
               "问题，发生了会如何，不发生又会如何。 既然如何， 问题的关键究竟为何？ 这种事实对本人来说意义重大，相信对这个世界也是有一定意义的。 那么， 生活中，若问题出现了，我们就不得不考虑它出现了的事实。 " \
               "既然如何， 可是，即使是这样，问题的出现仍然代表了一定的意义。 塞内加说过一句富有哲理的话，勇气通往天堂，怯懦通往地狱。这句话把我们带到了一个新的维度去思考这个问题: " \
               "希腊说过一句富有哲理的话，最困难的事情就是认识自己。这句话把我们带到了一个新的维度去思考这个问题: 我认为， 问题，到底应该如何实现。 所谓问题，关键是问题需要如何写。 " \
               "本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。 一般来说， 每个人都不得不面对这些问题。 在面对这种问题时， 黑格尔说过一句著名的话，只有永远躺在泥坑里的人，才不会再掉进坑里。这句话语虽然很短, " \
               "但令我浮想联翩。 "
    text1000000 = text1000*1000
    pressure = 10000
    dic = load_dictionary()
    print(len(dic))

    print('由于JPype调用开销巨大，以下速度显著慢于原生Java')
    # print("forwardSegment: ",end="")
    # evaluate_speed(forwardSegment, text2000, dic,pressure)
    # print("forwardSegment + trie: ", end="")
    # evaluate_speed(forwardSegment, text2000, trie,pressure)
    print("forwardSegment + trie + prefix speedup: ", end="")
    evaluate_speed(forwardSegment_prefix_speedup, text10, trie,pressure)
    evaluate_speed(forwardSegment_prefix_speedup, text10, dtrie, pressure)


