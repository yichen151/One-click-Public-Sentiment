"""爬取新浪新闻的类"""
# -*- coding: UTF-8 -*-
import aiohttp
import requests
import asyncio
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from data_process.character_remove import get_rid_blank


class XinLang:
    """爬取新浪新闻的类"""
    base_url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page='
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 '
    }
    name = 'xinlang'

    def __init__(self):
        self.texts = []  # 收集到的文本列表的列表
        self.urls = []  # 子页面url
        self.s = ''  # 最终产出的字符串

    def get_page_urls(self):
        """爬取滚动页面上的url"""
        data = []
        with ThreadPoolExecutor(10):
            for i in range(1, 11):
                url = self.base_url + f'{i}'
                response = requests.get(url, headers=self.headers)
                data.append(response.json()['result']['data'])
            for info in data:
                for dic in info:
                    self.urls.append(dic['url'])

    async def get_text(self, url):
        """爬取新闻页面中的文本"""
        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(url) as response:
                    html = await response.text()
                    tree = etree.HTML(html)
                    try:
                        title = tree.xpath('/html/body/div/h1[@class="main-title"]/text()')[0]
                    except IndexError:
                        title = ''
                    texts = tree.xpath('/html/body/*//p[@cms-style="font-L"]/text()')
                    if title:
                        texts.append(title)
                    if texts:
                        get_rid_blank(texts)
                        self.texts.append(texts)
        except aiohttp.ContentTypeError:
            pass

    async def text_main(self):
        """爬去文本，协程方法"""
        tasks = []
        for url in self.urls:
            task = asyncio.create_task(self.get_text(url))
            tasks.append(task)
        await asyncio.wait(tasks)

    def run(self):
        self.get_page_urls()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.text_main())
        for text in self.texts:
            for s in text:
                self.s += s
