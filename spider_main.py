
# - *- coding: utf- 8 - *-

#from baike_spider import url_manager, html_downloader, html_parser, html_outputer
import url_manager, html_downloader, html_parser, html_outputer

numOfUrlsMax = 10

class SpiderMain(object):

	def __init__(self):
		self.urlManger = url_manager.UrlManger()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		count = 1
		self.urlManger.add_new_url(root_url)

		while self.urlManger.has_new_url():
			#try:
				new_url = self.urlManger.get_new_url()
				print '[INFO] craw %d : %s' % (count, new_url)
				html_count = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url, html_count)

				self.urlManger.add_new_urls(new_urls) 
				self.outputer.collect_data(new_data)

				if count == numOfUrlsMax:
					break

				count = count + 1

			#except:
			#	print '[ERROR] craw failed, in spider_main:: craw()'

		self.outputer.output_html()



if __name__ == '__main__':
	root_url = "http://wiki.wargaming.net/en/Ship:Destroyers"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)







	#