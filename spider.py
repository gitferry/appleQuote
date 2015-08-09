#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry/appleQuote
author: Fangyu Gai <gaigai508@gmail.com>
date  : 08/09/2015
'''

import requests
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

def apple_spider(max_pages, index_url):
	page_index = 1
	apple_quote_collection = {}

	while page_index <= max_pages:
		url = index_url + 'go/dailyprice?p=' + str(page_index)
		html_text = requests.get(url).text

		soup = BeautifulSoup(html_text)

		for link in soup.findAll('a', {'class': 'rabel topic'}):
			topic_url = index_url + link.get('href')
			topic_title = link.string
			img_url_list = get_single_quote_list(topic_url)
			apple_quote_collection[topic_title] = img_url_list

		page_index += 1

	write_to_file(apple_quote_collection)

def get_single_quote_list(topic_url):
	html_text = requests.get(topic_url).text
	soup = BeautifulSoup(html_text)
	img_url_list = []

	for link in soup.findAll('img', {'class': 'external'}):
		img_url = link.get('src')
		img_url_list.append(img_url)

	return img_url_list


def write_to_file(collection):
	write_file = open('dailyprice.txt', 'w')

	for date, urls in collection.iteritems():
		line = date + ": " + ' '.join(urls) + '\n'
		write_file.write(line)

	write_file.close()


if __name__ == '__main__':
	max_pages = 10
	index_url = 'http://www.appletuan.com/'
	apple_spider(max_pages, index_url)
