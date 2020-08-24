from __future__ import absolute_import, print_function

import unittest

from pasteme import PasteMe
from pasteme.util import urljoin


class MyTestCase(unittest.TestCase):

    def test_get(self):
        pasteme: PasteMe = PasteMe(api_url='http://api.pasteme.cn/')
        response: str = pasteme.get('101', '123456')
        self.assertEqual('加密测试', response)

        response: dict = pasteme.get(101, 123456, json=True)
        self.assertEqual('加密测试', response['content'])

    def test_create(self):
        pasteme: PasteMe = PasteMe(api_url='http://api.pasteme.cn/')

        # response: dict = pasteme.create('Test', 'plain')
        # self.assertEqual(201, response['status'])
        #
        # response: str = pasteme.get(key=response['key'], password='password')
        # self.assertEqual('Test', response)

        response: dict = pasteme.create('Test', 'plain', password='password')
        self.assertEqual(201, response['status'])

        response: str = pasteme.get(key=response['key'], password='password')
        self.assertEqual('Test', response)

        response: dict = pasteme.create('Test', 'plain', 'create', 'password')
        self.assertEqual(201, response['status'])

        response: str = pasteme.get(key='create', password='password')
        self.assertEqual('Test', response)

    def test_urljoin(self):
        result: str = urljoin("https://api.pasteme.cn/", "101", "123456")
        self.assertEqual("https://api.pasteme.cn/101/123456", result)


if __name__ == '__main__':
    unittest.main()
