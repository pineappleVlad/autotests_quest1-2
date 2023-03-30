from unittest import TestCase
from quest2 import create_folder

class TestYandex(TestCase):
    def test_folder_exist(self):
        TOKEN = ''
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        path = 'testing'
        info, code = create_folder(TOKEN, path, URL)
        self.assertIn(path, info)


    def test_status_code(self):
        TOKEN = ''
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        path = 'testing'
        info, code = create_folder(TOKEN, path, URL)
        self.assertEqual(code, 201)

    def test_type(self):
        TOKEN = ''
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        path = 'testing'
        info, code = create_folder(TOKEN, path, URL)
        self.assertIsInstance(code, int)

    def test_for_bug(self):
        TOKEN = ''
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        path = 'testing'
        info, code = create_folder(TOKEN, path, URL)
        self.assertEqual(code, 404)