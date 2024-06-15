import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def convert_to_datetime(ms):
    timestamp_s = ms / 1000.0
    dt_object = datetime.fromtimestamp(timestamp_s)
    return (dt_object)

def get_my_band_list(token):
    url = f'https://openapi.band.us/v2.1/bands?access_token={token}'
    res = requests.get(url)
    if (res.status_code == 200):
        bands = res.json()
        return (bands['result_data']['bands'])
    else:
        raise Exception("유효하지 않은 밴드 토큰입니다.")

def get_title_from_url(url):
    if "band.us/band/" not in url:
        return (0)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    str = soup.title.string
    return (str[:-7])

def get_band_key(token, url):
    title = get_title_from_url(url)
    bands = get_my_band_list(token)
    for b in bands:
        if (b['name'] == title):
            return (b['band_key'])
    return (0)

def get_articles(token, band_key):
    url = f'https://openapi.band.us/v2/band/posts?access_token={token}&band_key={band_key}&locale=ko_KR'
    res = requests.get(url)
    if (res.status_code == 200):
        items = res.json()['result_data']['items']
        list = []
        for n, item in enumerate(items):
            article = {}
            article['number'] = n
            article['author'] = item['author']['name']
            article['subject'] = item['content'].split("\n")[0]
            article['content'] = item['content'].replace('\n', '<br>')
            article['id'] = item['post_key']
            article['created_at'] = convert_to_datetime(item['created_at'])
            list.append(article)
        return (list)
    else:
        print("Error: ", res.status_code)
        return (0)


def get_band_article(band_token, url):
    key = get_band_key(band_token, url)
    if key == 0:
        raise Exception("가입되지 않았거나 잘못된 밴드 URL입니다.")
    list = get_articles(band_token, key)
    if list == 0:
        raise Exception("목록을 가져오는 데 실패하였습니다.")
    return (list)
