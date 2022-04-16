# -*- coding: UTF-8 -*-
from data_class.weibo import WeiBo
from data_class.xinlang import XinLang
from data_process.cut_count import CutCount
from data_process.cloud import Cloud
from log.log import save_log


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
