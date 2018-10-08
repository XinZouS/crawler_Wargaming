
# - *- coding: utf- 8 - *-

class HtmlOutputer(object):
	def __init__(self):
		self.datas = []

	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)


	def output_html(self):
		fout = open('output.html', 'w') # 写文件

		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table>")

		# ASCII is data format, parse into utf-8
		for data in self.datas:
			fout.write("<tr>")
			title = "---"
			tier = "---"
			url = "---"
			if 'title' in data:
				title = data['title'].encode('utf-8')
			if 'tier' in data:
				tier  = data['tier'].encode('utf-8')
			if 'url' in data:
				url   = data['url']
			if title == "---" or tier == "---" or url == "---":
				continue
			fout.write("<td>%s</td>" % title)
			fout.write("<td>%s</td>" % tier)
			fout.write("<td>%s</td>" % url)

			fout.write("</tr>")

		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")

		fout.close()
