"""历史数据保存和检测的函数"""
# -*- coding: UTF-8 -*-
import os
import datetime


def save_log(d_class, cut, cloud):
    """这个函数传入要保存的类和CutCount, Cloud两个类自动根据当前时间存放在log下的文件夹"""
    date = datetime.datetime.today()
    path = f'\\{d_class.name} {date.date()} {date.hour} {date.minute}'
    folder = os.getcwd() + path
    is_exists = os.path.exists(folder)
    if not is_exists:
        os.makedirs(folder)
        cut_path = folder + '/count.json'
        cloud_path = folder + '/cloud.jpg'
        cut.save(cut_path)
        cloud.save(cloud_path)

    return is_exists


def is_log(d_class):
    """根据对应文件夹是否存在来控制爬取频率：10分钟一次"""
    date = datetime.datetime.today()
    for i in range(0, 11):
        path = f'\\{d_class.name} {date.date()} {date.hour} {date.minute - i}'
        folder = os.getcwd() + path
        is_exists = os.path.exists(folder)
        if is_exists:
            return False

