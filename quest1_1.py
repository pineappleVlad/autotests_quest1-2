
def filtred(geo_logs):
    result_logs = []
    for i in geo_logs:
        for key, value in i.items():
            if 'Россия' in value:
                result_logs.append(i)
    return result_logs

def max_channel(stats):
    max_digit = 0
    for key, value in stats.items():
        if max_digit < value:
            max_digit = value
            channel = key
    return channel

def unique(ids):
    result = []
    for key, value in ids.items():
        for i in value:
            if i not in result:
                result.append(i)
    return result


if __name__ == '__main__':
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
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}


    print(filtred(geo_logs))
    print(max_channel(stats))
    print(unique(ids))