from __future__ import absolute_import, print_function

import unittest
from pasteme import PasteMe


class MyTestCase(unittest.TestCase):

    def test_get(self):
        pasteme: PasteMe = PasteMe(api_url='http://api.pasteme.cn/')
        response: str = pasteme.get('101', '123456')
        self.assertEqual('加密测试', response)

        response: dict = pasteme.get(101, 123456, json=True)
        self.assertEqual('加密测试', response['content'])

    def test_create(self):
        pasteme: PasteMe = PasteMe(api_url='http://api.pasteme.cn/')

        response: dict = pasteme.create('Test', 'plain')
        self.assertEqual(201, response['status'])

        response: dict = pasteme.create('Test', 'plain', 'create', 'password')
        self.assertEqual(201, response['status'])

        response: str = pasteme.get(key='create', password='password')
        self.assertEqual('Test', response)


if __name__ == '__main__':
    unittest.main()
