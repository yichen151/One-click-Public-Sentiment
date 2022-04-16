"""
历史数据保存和检测的函数
文件和文件夹路径以run.py为基准
"""
# -*- coding: UTF-8 -*-
import os
import datetime
import json


def save_log(d_class, cut, cloud):
    """这个函数传入要保存的类和CutCount, Cloud两个类自动根据当前时间存放在log下的文件夹"""
    date = datetime.datetime.today()
    folder = f'./log/{d_class.name} {date.date()} {date.hour} {date.minute}'
    is_exists = os.path.exists(folder)
    if not is_exists:
        os.makedirs(folder)
        cut_path = folder + '/count.json'
        cloud_path = folder + '/cloud.jpg'
        cut.save(cut_path)
        cloud.save(cloud_path)

    return is_exists


def is_log(d_class):
    """根据对应文件夹是否存在来控制爬取频率"""
    date = datetime.datetime.today()
    folder = f'./log/{d_class.name} {date.date()} {date.hour} {date.minute}'
    is_exists = os.path.exists(folder)
    if is_exists:
        return True
    return False


def get_log():
    """读取数据文件夹列表并返回"""
    dirs = os.listdir('./log/')
    dirs.remove('log.py')
    dirs.remove('__pycache__')
    dirs.sort(reverse=True)
    return dirs


def get_current_log(name, cnt):
    """获取最新得到的数据，并返回处理后的字符串和图片路径"""
    dirs = get_log()
    if name == 'XinLang':
        folder = dirs[0]
    else:
        i = 0
        for item in dirs:
            if item[:5] != 'weibo':
                i += 1
        folder = dirs[i]
    path = './log/' + folder
    cloud_path = path + '/cloud.jpg'
    count_path = path + '/count.json'
    with open(count_path, 'r', encoding='utf-8') as fp:
        dirt = json.load(fp)
    s = ''
    i = 0
    for key, value in dirt.items():
        s += key
        s += ':'
        s += str(value)
        s += '\n'
        i += 1
        if i == cnt:
            break
    return s, cloud_path
