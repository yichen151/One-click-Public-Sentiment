#!.\venv\Scripts\python.exe
"""生成词云的类"""
# -*- coding: UTF-8 -*-
import wordcloud
import random
import matplotlib.pyplot as plt


class Cloud:
    """生成词云的类"""
    masks = [
        './data_process/resource/mask1.jpg',
        './data_process/resource/mask2.jpg',
    ]
    fonts = [
        './data_process/resource/font1/HuaGuangGangTieZhiHei-KeBianTi-2.ttf',
        './data_process/resource/font2/WenYue-ShengHuoJiaTi-J-2.otf'
    ]

    def __init__(self, s):
        """根据字符串自动生成词云"""
        font = self.fonts[random.randint(0, 1)]  # 从字体中随机选一个
        mask_path = self.masks[random.randint(0, 1)]  # 从背景图中随机选一个
        mask = plt.imread(mask_path)
        stop_file = './data_process/resource/stop_list.txt'
        stop_words = set()
        # 读取停用词
        stop_list = [line.strip() for line in open(stop_file, 'r', encoding='utf-8').readlines()]
        stop_words.update(stop_list)
        self.cloud = wordcloud.WordCloud(
            font_path=font,
            background_color='white',
            mask=mask,
            max_words=500,
            max_font_size=200,
            stopwords=stop_words
        )
        self.cloud.generate(s)

    def save(self, path):
        """保存词云图"""
        self.cloud.to_file(path)
