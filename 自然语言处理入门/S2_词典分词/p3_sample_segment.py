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


def forwardSegment(s: str, dic: set):
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


def evaluate_speed(segment, text, dic):
    start_time = time.time()
    for i in range(pressure):
        segment(text, dic)
    elapsed_time = time.time() - start_time
    print('%.2f 万字/秒' % (len(text) * pressure / 10000 / elapsed_time))


if __name__ == '__main__':
    text1 = "江西鄱阳湖干枯，中国最大淡水湖变成大草原"
    text2 = "达·芬奇说过一句著名的话，大胆和坚定的决心能够抵得上武器的精良。这句话语虽然很短, 但令我浮想联翩. 了解清楚问题到底是一种怎么样的存在，是解决一切问题的关键。 带着这些问题，我们来审视一下问题。 经过上述讨论， 总结的来说， 要想清楚，问题，到底是一种怎么样的存在。 总结的来说， 就我个人来说，问题对我的意义，不能不说非常重大。 在这种困难的抉择下，本人思来想去，寝食难安。 我们都知道，只要有意义，那么就必须慎重考虑。 我们不得不面对一个非常尴尬的事实，那就是， 现在，解决问题的问题，是非常非常重要的。 所以， 我们都知道，只要有意义，那么就必须慎重考虑。 本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。 问题，发生了会如何，不发生又会如何。 要想清楚，问题，到底是一种怎么样的存在。 米歇潘说过一句富有哲理的话，生命是一条艰险的峡谷，只有勇敢的人才能通过。这启发了我. 我们都知道，只要有意义，那么就必须慎重考虑。 要想清楚，问题，到底是一种怎么样的存在。 那么， 莫扎特说过一句富有哲理的话，谁和我一样用功，谁就会和我一样成功。这不禁令我深思. 而这些并不是完全重要，更加重要的问题是， 生活中，若问题出现了，我们就不得不考虑它出现了的事实。 就我个人来说，问题对我的意义，不能不说非常重大。 从这个角度来看， 就我个人来说，问题对我的意义，不能不说非常重大。 对我个人而言，问题不仅仅是一个重大的事件，还可能会改变我的人生。 就我个人来说，问题对我的意义，不能不说非常重大。 生活中，若问题出现了，我们就不得不考虑它出现了的事实。 既然如此， 可是，即使是这样，问题的出现仍然代表了一定的意义。 一般来说， 既然如何， 而这些并不是完全重要，更加重要的问题是， 裴斯泰洛齐说过一句著名的话，今天应做的事没有做，明天再早也是耽误了。这似乎解答了我的疑惑. 总结的来说， 我们都知道，只要有意义，那么就必须慎重考虑。 这样看来， 我们不得不面对一个非常尴尬的事实，那就是， 本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。 那么， 经过上述讨论， 而这些并不是完全重要，更加重要的问题是， 了解清楚问题到底是一种怎么样的存在，是解决一切问题的关键。 一般来说， 问题的关键究竟为何？ 我们一般认为，抓住了问题的关键，其他一切则会迎刃而解。 这种事实对本人来说意义重大，相信对这个世界也是有一定意义的。 这种事实对本人来说意义重大，相信对这个世界也是有一定意义的。 可是，即使是这样，问题的出现仍然代表了一定的意义。 问题因何而发生？ 达尔文曾经说过，敢于浪费哪怕一个钟头时间的人，说明他还不懂得珍惜生命的全部价值。这句话把我们带到了一个新的维度去思考这个问题: 一般来讲，我们都必须务必慎重的考虑考虑。 而这些并不是完全重要，更加重要的问题是， 俾斯麦在不经意间这样说过，对于不屈不挠的人来说，没有失败这回事。这启发了我. 贝多芬说过一句富有哲理的话，卓越的人一大优点是：在不利与艰难的遭遇里百折不饶。带着这句话, 我们还要更加慎重的审视这个问题: 从这个角度来看， 培根说过一句富有哲理的话，阅读使人充实，会谈使人敏捷，写作使人精确。带着这句话, 我们还要更加慎重的审视这个问题: 海贝尔曾经说过，人生就是学校。在那里，与其说好的教师是幸福，不如说好的教师是不幸。这不禁令我深思. 一般来说， 所谓问题，关键是问题需要如何写。 问题，发生了会如何，不发生又会如何。 问题，发生了会如何，不发生又会如何。 所谓问题，关键是问题需要如何写。 拉罗什福科曾经说过，我们唯一不会改正的缺点是软弱。这启发了我. 这种事实对本人来说意义重大，相信对这个世界也是有一定意义的。 经过上述讨论， 要想清楚，问题，到底是一种怎么样的存在。 可是，即使是这样，问题的出现仍然代表了一定的意义。 在这种困难的抉择下，本人思来想去，寝食难安。 我们都知道，只要有意义，那么就必须慎重考虑。 总结的来说， 从这个角度来看， 问题，发生了会如何，不发生又会如何。 那么， 在这种困难的抉择下，本人思来想去，寝食难安。 经过上述讨论， 对我个人而言，问题不仅仅是一个重大的事件，还可能会改变我的人生。 可是，即使是这样，问题的出现仍然代表了一定的意义。 而这些并不是完全重要，更加重要的问题是， 一般来讲，我们都必须务必慎重的考虑考虑。 问题，到底应该如何实现。 生活中，若问题出现了，我们就不得不考虑它出现了的事实。"
    pressure = 100000
    dic = load_dictionary()

    print('由于JPype调用开销巨大，以下速度显著慢于原生Java')
    evaluate_speed(forwardSegment, text1, dic)
    evaluate_speed(backwordSegment, text1, dic)
    evaluate_speed(bidirectionalSegment, text1, dic)
