from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def get_html(driver):
    driver.get("https://www.naver.com")

    search_box = driver.find_element(By.XPATH, '//*[@id="query"]')

    search_box.send_keys("SAP 컨설턴트 채용")
    search_box.send_keys(Keys.RETURN)

    driver.find_element(By.XPATH, '//*[@id="main_pack"]/section[1]/div/div[6]/a').click()
    # driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/section/div[1]/div/div[2]/a[3]').click()
    sleep(3)

    for i in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        
    html = driver.page_source
    return html

from bs4 import BeautifulSoup

def get_recruit_from_naver(html):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', 'recruit_wrap')
    recruit_list = []
    for d in divs:
        recruit = {}
        recruit['title'] = d.find('a', 'title').text
        recruit['subtitle'] = d.find('div', 'sub_title').text
        recruit['tags'] = []
        recruit['keywords'] = []
        recruit['link'] = d.find('a', 'link_site')['href']
        tags = d.find_all('span', 'item')
        keywords = d.find_all('a', 'link_keyword')
        for tag in tags:
            recruit['tags'].append(tag.text)
        if ("까지" in recruit['tags'][-1])
            recruit['tags'].pop()
        for keyword in keywords:
            recruit['keywords'].append(keyword.text)
        recruit_list.append(recruit)
    return (recruit_list)

from datetime import datetime

def make_article(size, recruit_list):
    recruit_list = recruit_list[:size]
    article = {}
    now = datetime.now()
    article['subject'] = now.strftime("[SAP 컨설턴트 및 ABAP 채용공고] %Y년%m월%d일 %H시(30건)")
    concat = ""
    for content in recruit_list:
        concat += f"""
제목: {content['title']}
부제: {content['subtitle']}
"""
        for tag in content['tags']:
            concat += "- " + tag + "\n"
        for keyword in content['keywords']:
            concat += "- " + keyword + "\n"
        concat += "링크: " + content['link'] + "\n"
    article['content'] = concat.replace('\n', '<br>')
    return (article)


def get_naver_search(size, driver):
    html = get_html(driver)
    recruit_list = get_recruit_from_naver(html)
    article = make_article(size, recruit_list)
    return (article)
