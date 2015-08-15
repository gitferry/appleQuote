import requests
import sys
import datetime

from bs4 import BeautifulSoup

import os
import re
reload(sys)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
sys.setdefaultencoding('utf-8')

import django
django.setup()

from quote.models import Quote, Image


def apple_spider(max_pages, index_url):
	page_index = 1
	apple_quote_collection = []

	while page_index <= max_pages:
		url = index_url + 'go/dailyprice?p=' + str(page_index)
		html_text = requests.get(url).text

		soup = BeautifulSoup(html_text)

		for link in soup.findAll('a', {'class': 'rabel topic'}):
			single_topic = {}

			topic_url = index_url + link.get('href')
			topic_title = link.string

			print link.string

			date_string = '-'.join(re.findall(r'[0-9]+', topic_title)[:3])
			print date_string
			if not date_string:
				continue

			try:
				topic_date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
			except:
				pass

			quote, created = Quote.objects.get_or_create(title = topic_title, pub_date = topic_date)

			if not created:
				print 'The spider is finished, the quotes list is latest. :)'
				return

			images_list = get_single_quote_list(topic_url)

			for url in images_list:
				quote.image_set.create(url = url)


		page_index += 1

	# write_to_db(apple_quote_collection)

def get_single_quote_list(topic_url):
	html_text = requests.get(topic_url).text
	soup = BeautifulSoup(html_text)
	img_url_list = []

	for link in soup.findAll('img', {'class': 'external'}):
		img_url = link.get('src')
		img_url_list.append(img_url)

	return img_url_list


def write_to_db(collection):

	for title, urls in collection.iteritems():
		quote = Quote(title=title)

		for url in urls:
			img_url = ImgUrl(image_url=url)
			img_url.save()
			quote.image_urls = img_url
		quote.save()


if __name__ == '__main__':
	max_pages = 10
	index_url = 'http://www.appletuan.com/'
	apple_spider(max_pages, index_url)
