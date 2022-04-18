"""挖掘微博评论的类"""
# -*- coding: UTF-8 -*-
from asyncio import get_event_loop, wait, create_task
from aiohttp import ClientSession, ClientConnectionError, ClientConnectorError
from requests import get
from data_process.character_remove import get_rid


class WeiBo:
    """挖掘微博评论的类"""
    first_url = 'https://weibo.com/ajax/feed/hottimeline?since_id=0&group_id=1028039999&containerid=102803_ctg1_9999_' \
                '-_ctg1_9999_home&extparam=discover"|new_feed&max_id=0&count=10'
    refer = 'https://weibo.com/newlogin?tabtype=list&gid=1028039999&url=https://weibo.com/?category=1760'
    first_params = {
        'since_id': 0,
        'group_id': 1028039999,
        'containerid': '102803_ctg1_9999_-_ctg1_9999_home',
        'extparam': 'discover|new_feed',
        'max_id': 0,
        'count': 10
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 ',
        'referer': refer,
    }
    name = 'weibo'

    def __init__(self):
        self.comments_lists = []  # 评论的列表
        self.s = ''  # 最终产出的字符串

    def get_text(self):
        """对第一个页面进行读取，返回的是第一个页面的评论的列表"""
        texts = []
        with get(self.first_url, headers=self.headers, params=self.first_params) as response:
            dic = response.json()
            comments = dic['statuses']
            for comment in comments:
                text_raw = comment['text_raw']
                text = get_rid(text_raw)
                texts.append(text)

        self.comments_lists.append(texts)

    async def get_text_(self, url, params):
        """对第二次及以后的刷新进行读取，返回的是每次刷新到的评论列表"""
        texts = []
        try:
            async with ClientSession(headers=self.headers) as session:
                async with session.get(url, params=params) as response:
                    dic = await response.json()
                    comments = dic['statuses']
                    for comment in comments:
                        text_raw = comment['text_raw']
                        text = get_rid(text_raw)
                        texts.append(text)
            self.comments_lists.append(texts)
        except ClientConnectorError and ClientConnectionError:
            pass

    async def main(self):
        """挖掘子页面，协程方法"""
        tasks = []
        for i in range(2, 51):
            refresh_url = 'https://weibo.com/ajax/feed/hottimeline?refresh=2&group_id=1028039999&containerid' \
                          f'=102803_ctg1_9999_-_ctg1_9999_home&extparam=discover|new_feed&max_id={i}&count=10'
            refresh_params = {
                'refresh': 2,
                'group_id': 1028039999,
                'containerid': '102803_ctg1_9999_-_ctg1_9999_home',
                'extparam': 'discover|new_feed',
                'max_id': i,
                'count': 10
            }
            task = create_task(self.get_text_(refresh_url, params=refresh_params))
            tasks.append(task)
        await wait(tasks)

    def run(self):
        """挖掘首页面，调用协程挖掘子页面"""
        self.get_text()
        loop = get_event_loop()
        loop.run_until_complete(self.main())
        for comment_list in self.comments_lists:
            for comment in comment_list:
                self.s += comment
