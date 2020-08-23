from __future__ import absolute_import, print_function

import requests


class PasteMe(object):

    def __init__(self, api_url: str = 'http://api.pasteme.cn/', token: str = ''):
        self.api_url = api_url
        self.token = token

    def get(self, key: [int, str], password: [int, str] = None, json: bool = False) -> [dict, str]:
        """
        根据 key 读取 Paste
        :param key: Paste ID
        :param password: 密码，没有则留空
        :param json: 是否请求 json response，如果为 false 则只返回 content 字段
        :return: {
            "status": 200,
            "lang": "bash",
            "content": "echo Hello"
        }
        """

        url: str = f'{self.api_url}{key}{"" if password is None else ",{}".format(password)}?json={str(json).lower()}'
        response: requests.Response = requests.api.get(url=url)

        return response.json() if json else response.content.decode('utf-8')

    def create(self, content: str, lang: str, key: str = None, password: str = None, read_once: bool = False) -> dict:
        """
        创建一个 Paste
        :param content: Paste 的内容
        :param lang: Paste 的高亮类型
        :param key: Paste ID，如果留空则自动生成，非空的时候会自动变为阅后即焚的 Paste
        :param password: 密码，留空则不设置
        :param read_once: 阅后即焚
        :return: {
            "status": 201,
            "key": <paste id>
        }
        """

        json_param = {
            'content': content,
            'lang': lang
        }

        if password is not None and len(password) != 0:
            json_param['password'] = password

        if read_once:
            response: requests.Response = requests.api.post(url=f'{self.api_url}once', json=json_param)
        elif key is None or len(key) == 0:
            response: requests.Response = requests.api.post(url=self.api_url, json=json_param)
        else:
            response: requests.Response = requests.api.put(url=f'{self.api_url}{key}', json=json_param)

        return response.json()
