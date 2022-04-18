#!.\venv\Scripts\python.exe
"""文本处理函数"""
# -*- coding: UTF-8 -*-
from re import compile, sub
BracketsRe = compile(r'\[.*?]')  # 中括号表情
UrlRe = compile(r'http://.*')  # 网址
SymbolRe = compile(r"#|@|【|】|《|》|")  # 字符
BlankRe = compile(r'\s')  # 空白符
expressions = [BracketsRe, UrlRe, SymbolRe]


def get_rid(text):
    """处理评论，去除表情链接和一些特殊字符"""
    for expression in expressions:
        text = sub(expression, '', text)
    return text


def get_rid_blank(texts):
    """去掉空格"""
    for text in texts:
        sub(BlankRe, '', text)
