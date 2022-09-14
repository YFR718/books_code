# -*- coding:utf-8 -*-
# 《自然语言处理入门》2.3
import time

from 自然语言处理入门.S2_词典分词.p2_utility import load_dictionary

dic = load_dictionary()


def fullySegment(s: str, dic: set):
    ans = []
    for l in range(len(s) - 1):
        for r in range(l + 1, len(s)):
            word = s[l:r]
            if word in dic:
                ans.append(word)
    return ans


def forwardSegment(s: str, dic):
    ans = []
    l = 0
    while l < len(s):
        for r in range(len(s), l, -1):
            word = s[l:r]
            # find the longest word
            if word in dic:
                ans.append(word)
                l += len(word)
                break
            # not match start with l
            if r == l + 1:
                l += 1
    return ans


def backwordSegment(s: str, dic: set):
    ans = []
    r = len(s)
    while r > 0:
        for l in range(r):
            word = s[l:r]
            # find the longest word
            if word in dic:
                ans.append(word)
                r -= len(word)
                break
            # not match start with r
            if l == r - 1:
                r -= 1
    ans.reverse()
    return ans


def bidirectionalSegment(s: str, dic: set):
    f = forwardSegment(s, dic)
    b = backwordSegment(s, dic)
    if len(f) > len(b):
        return len(b)
    elif len(f) < len(b):
        return len(f)
    else:
        singleF = len([w for w in f if len(w) == 1])
        singleB = len([w for w in b if len(w) == 1])
        if singleF < singleB:
            return f
        else:
            return b


def evaluate_speed(segment, text, dic,pressure):
    start_time = time.time()
    for i in range(pressure):
        segment(text, dic)
    elapsed_time = time.time() - start_time
    print('%.2f 万字/秒' % (len(text) * pressure / 10000 / elapsed_time))


if __name__ == '__main__':
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
    pressure = 10
    dic = load_dictionary()

    print('由于JPype调用开销巨大，以下速度显著慢于原生Java')
    evaluate_speed(forwardSegment, text1000, dic,pressure)
    evaluate_speed(backwordSegment, text1000, dic,pressure)
    evaluate_speed(bidirectionalSegment, text1000, dic,pressure)
