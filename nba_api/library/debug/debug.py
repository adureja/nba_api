import os
from lxml.html import fromstring
import random
import requests
from itertools import cycle
import traceback
DEBUG = False

# Saving and loading responses from text files so that you do not have to do multiple requests when debugging.
DEBUG_STORAGE = False

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:19]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies



PROXY = get_proxies()

# STATS_HEADERS = {}
