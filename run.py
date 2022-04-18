"""整合数据爬取和处理函数run"""
# -*- coding: UTF-8 -*-
from weibo import WeiBo
from xinlang import XinLang
from cut_count import CutCount
from cloud import Cloud
from log import save_log


def run(name):
    """
    运行函数，传入要运行的源名称
    WeiBo设定运行30秒左右，XinLang设定运行1分钟左右
    """
    # 检测类别
    if name == 'WeiBo':
        target = WeiBo()
    else:
        target = XinLang()
    # 运行爬取
    target.run()
    # 执行分词
    cut = CutCount()
    cut.cut_words(target.s)
    # 生成词云
    cloud = Cloud(target.s)
    # 保存数据
    save_log(target, cut, cloud)
