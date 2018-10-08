# - *- coding: utf- 8 - *-

import urllib2

class HtmlDownloader(object):
	

	def download(self, url):
		if url is None:
			return None

		response = urllib2.urlopen(url)

		getcode = response.getcode()
		if getcode != 200:
			print "[ERROR] HtmlDownloader:: getcode = %d, failed url = %s" % (getcode, url)
			return None

		return response.read()


