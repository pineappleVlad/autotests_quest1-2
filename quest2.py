import requests

def create_folder(token, path, url):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    new_url = f'{url}?path={path}'
    info = requests.get(new_url, headers=headers).text
    if path in info:
        requests.delete(new_url, headers=headers)
    result = requests.put(new_url, headers=headers)
    code = result.status_code
    res_info = requests.get(new_url, headers=headers).text
    return res_info, code


if __name__ == '__main__':
    TOKEN = ''
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    path = 'testing'
    res_info, code = create_folder(TOKEN, path, URL)
    print(res_info)
    print(code)