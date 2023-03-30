from unittest import TestCase
from quest1_1 import unique, filtred, max_channel

class TestFiltred(TestCase):
    def test_len(self):
        geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]
        res = filtred(geo_logs)
        self.assertEqual(len(res), 6)

    def test_type(self):
        geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']}
        ]
        res = filtred(geo_logs)
        self.assertIsInstance(res, list)

    def test_name_result(self):
        geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']}
        ]
        res = filtred(geo_logs)
        for i in res:
            for key, value in i.items():
                self.assertIn('Россия', value)


class TestUnique(TestCase):
    def test_numbers(self):
        ids = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}
        res = unique(ids)
        self.assertEqual(len(res), 6)

    def test_type(self):
        ids = {'user1': [1, 1, 2, 2, 3]}
        res = unique(ids)
        self.assertIsInstance(res, list)

    def test_unique(self):
        ids = {'user1': [1, 1, 2, 2, 3]}
        unique_ids = [1, 2, 3]
        res = unique(ids)
        self.assertEqual(res, unique_ids)


class TestMaxChannel(TestCase):
    def test_base(self):
        stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
        res = max_channel(stats)
        self.assertEqual(res, 'yandex')

    def test_else_name(self):
        stats = {'google': 10, 'vk': 20, 'ok': 5}
        res = max_channel(stats)
        self.assertEqual(res, 'vk')

    def test_types(self):
        stats = {'google': 10, 'vk': 20, 'ok': 5}
        res = max_channel(stats)
        self.assertIsInstance(res, str)
