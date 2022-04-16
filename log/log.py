"""
历史数据保存和检测的函数
文件和文件夹相对路径以run.py为基准
"""
# -*- coding: UTF-8 -*-
import os
import datetime
import json
import re


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


def is_log(name):
    """
    根据对应文件夹是否存在来控制爬取频率
    若存在则直接显示相应文件夹
    """
    date = datetime.datetime.today()
    folder = f'./log/{name} {date.date()} {date.hour} {date.minute}'
    is_exists = os.path.exists(folder)
    if is_exists:
        return folder
    else:
        return None


def get_log():
    """读取数据文件夹列表（升序）并返回"""
    dirs = os.listdir('./log/')
    dirs.remove('log.py')
    dirs.remove('__pycache__')
    dirs.sort()
    return dirs


def get_current_log(name, cnt):
    """获取最新得到的数据，并返回处理后的字符串和图片路径"""
    dirs = get_log()
    if name == 'XinLang':
        # 新浪直接取最后一个
        i = -1
        while dirs[i][:7] == 'xinlang':
            i -= 1
        folder = dirs[i + 1]
    else:
        # 微博要查找
        i = 0
        for item in dirs:
            if item[:5] == 'weibo':
                i += 1
        folder = dirs[i - 1]
    path = './log/' + folder
    cloud_path = path + '/cloud.jpg'
    count_path = path + '/count.json'
    with open(count_path, 'r', encoding='utf-8') as fp:
        dirt = json.load(fp)
    s = ''
    i = 0
    for key, value in dirt.items():
        s += key + ':' + str(value) + '\n'
        i += 1
        if i == cnt:
            break
    return s, cloud_path


def get_history_log():
    """获取历史最新的十个文件夹"""
    pattern = re.compile(r' (?P<time>20.*)')
    dirs = get_log()
    i = 0
    lis = []
    for item in dirs:
        se = re.search(pattern, item)
        time = se.group('time')
        lis.append((time, i))
        i += 1
    # 将时间和编号的元组列表降序排序
    for i in range(len(lis) - 1):
        min_ = i
        for j in range(i + 1, len(lis)):
            if lis[j][0] > lis[min_][0]:
                min_ = j
                lis[min_], lis[i] = lis[i], lis[min_]
    re_list = [dirs[comb[1]] for comb in lis[:10]]
    return re_list


def get_exact_log(log_name, cnt):
    path = './log/' + log_name
    cloud_path = path + '/cloud.jpg'
    count_path = path + '/count.json'
    with open(count_path, 'r', encoding='utf-8') as fp:
        dirt = json.load(fp)
    s = ''
    i = 0
    for key, value in dirt.items():
        s += key + ':' + str(value) + '\n'
        i += 1
        if i == cnt:
            break
    return s, cloud_path
