# - *- coding: utf- 8 - *-

from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):

	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		# get part of link: <a href="/en/Ship:Nicholas" title="Ship:Nicholas">Nicholas</a>
		links = soup.find_all('a', href = re.compile(r"/en/Ship"))
		print """
			[INFO] from url: %s 
			       _get_new_urls() num of links = %d
			""" % (page_url, len(links))
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url, new_url) # 把2个url拼接成对应的完整url
			new_urls.add(new_full_url)
		return new_urls


	def _get_new_data(self, page_url, soup):
		res_data = {} # Dictionary
		try:
			# url:
			res_data['url'] = page_url
			# 获取标题： <div class="b-description gw-frame-1">
			title_node = soup.find('div', class_ = "b-description gw-frame-1").find('p').find('strong')
			titleText = title_node.get_text()
			res_data['title'] = titleText
			print "get title = %s" % titleText
			# 获取摘要：<div class="b-description gw-frame-1">
			tier_node = soup.find('div', class_ = "b-description gw-frame-1").find('div', class_ = "l-description-img_class").find('span', class_ = "b-description-img_class")
			tierText = tier_node.get_text()
			res_data['tier'] = tierText
			print "get Tier = %s" % tierText

		except:
			print "[ERROR] unable to get_new_data, will skip url: %s" % page_url

		return res_data


	def parse(self, page_url, html_count):
		if page_url is None or html_count is None:
			print "[ERROR] unable to parse, page_url = %s, html_count = %d" % (page_url, len(html_count))
			return

		#soup = BeautifulSoup(html_count, 'html.parser', from_encoding = 'utf-8')
		soup = BeautifulSoup(html_count, 'html.parser')
		new_urls = self._get_new_urls(page_url, soup)
		new_data = self._get_new_data(page_url, soup)
		return new_urls, new_data


