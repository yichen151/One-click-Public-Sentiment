"""对字符串进行分词的类"""
# -*- coding: UTF-8 -*-
import jieba
import json
from collections import Counter


class CutCount:
    """对字符串进行分词的类"""

    def __init__(self):
        self.words = ''  # 切分后的字符串
        self.count = []  # 词频统计后的得到的元组列表
        stop_file = './data_process/resource/stop_list.txt'
        self.stop_list = [line.strip() for line in open(stop_file, 'r', encoding='utf-8').readlines()]

    def cut_words(self, s):
        """使用jieba进行分词"""
        word_count = Counter()
        # 加入一些网络热门词
        user_dict = './data_process/resource/user_dict.txt'
        jieba.load_userdict(user_dict)
        words_list = jieba.lcut(s, HMM=True, cut_all=True)
        self.words = ' '.join(words_list)
        for word in words_list:
            if len(word) > 1 and word not in self.stop_list:
                word_count[word] += 1
        self.count = word_count.most_common(15)

    def save(self, path):
        """将词频信息保存"""
        dic = dict(self.count)
        with open(path, mode='w', encoding='utf-8') as f:
            json.dump(dic, fp=f, indent=4)
