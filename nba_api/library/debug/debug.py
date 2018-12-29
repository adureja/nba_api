import os
from bs4 import BeautifulSoup
import html5lib
import random
import re
import requests
DEBUG = False

# Saving and loading responses from text files so that you do not have to do multiple requests when debugging.
DEBUG_STORAGE = False

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    # proxies = set()
    proxy_rows = [i.find_parent('tr') for i in soup(text=re.compile(r'yes'))]
    proxies = set([':'.join([x.getText() for x in i.findAll('td')[:2]]) for i in proxy_rows])
    # for i in parser.xpath('//tbody/tr')[:19]:
    #     if i.xpath('.//td[7][contains(text(),"yes")]'):
    #         proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
    #         proxies.add(proxy)
    #         print proxy
    # for p in proxy_rows:
    # 	proxy = ""
    print(proxies)
    return proxies



PROXY = get_proxies()

# STATS_HEADERS = {}
