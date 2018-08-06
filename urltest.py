import HTMLParser
import urllib
urlText=[]
class parseText(HTMLParser.HTMLParser):
	def handle_data(self, data):
		if data != '\n' :
			urlText.append(data)
lParser = parseText()

thisurl ="http://www.codeinks.com"
#Feed HTML file into parsers
lParser.feed(urllib.request.urlopen(thisurl).read().decode('utf8'))
lParser.close()
for item in urlText:
    print (item)
