import re
import requests
from tqdm import tqdm


from fields import fields
from utils import *

host = 'http://www.yaopinnet.com'


def fetch_item(sess, url):
    resp = sess.get(url)
    resp.encoding = resp.apparent_encoding
    pattern = '<li class=\"smsli\">((.|\s)*?)</li>'
    groups = re.findall(pattern, resp.text)
    items = [group[0] for group in groups]
    drug_info = {}
    for item in items:
        # clean
        parse_rules = [
            {'from': '<br\s*/?>', 'to': ' '},
            {'from': '\s+', 'to': ' '},
            {'from': '(?<=(】|。|：|；))\s*', 'to': ''},
            {'from': '．', 'to': '.'},
        ]
        for t in parse_rules:
            item = re.sub(t['from'], t['to'], item)
        # extract
        for field in fields:
            if '【{}】'.format(field['name']) in item:
                drug_info[field['field_name']] = re.findall(field['extract_rule'], item)[0]
                break
    return drug_info


def fetch_items():
    urls = []
    with open('urls.txt', 'r') as f:
        urls = [line.strip() for line in f.readlines()]
    sess = requests.Session()
    drug_infos = []
    for url in tqdm(urls[11577:]):
        drug_infos.append(fetch_item(sess, url))
    save_drugs_to_file(drug_infos)


def fetch_urls():
    start_url = host + '/tools/sms.asp'
    sess = requests.Session()
    resp = sess.get(start_url)
    # fetch all categories
    resp.encoding = resp.apparent_encoding
    pattern = '<a href=\"(/\w+/[a-z]\d\.html?)\"'
    category_urls = [host + url for url in re.findall(pattern, resp.text)]
    page_urls = []
    for url in tqdm(category_urls):
        page_urls.append(url)
        resp = sess.get(url)
        resp.encoding = resp.apparent_encoding
        pattern = '<a href=\'(/\w+/[a-z]\d+\.html?)\'>'
        page_urls += [host + url for url in re.findall(pattern, resp.text)]
    item_urls = []
    for url in tqdm(page_urls):
        resp = sess.get(url)
        resp.encoding = resp.apparent_encoding
        pattern = '<li><a href=\'(/\w+/[a-zA-z0-9]*.htm)\'>'
        item_urls += [host + url for url in re.findall(pattern, resp.text)]
    with open('urls.txt', 'w') as f:
        for url in tqdm(item_urls):
            f.write('{}\n'.format(url))


if __name__ == '__main__':
    fetch_urls()
    # fetch_items()
