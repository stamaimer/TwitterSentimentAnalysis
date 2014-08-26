# -*- coding: utf-8 -*-

import re
import codecs
import requests

file = codecs.open('urls', 'r', 'utf-8') 

payload = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36', 'cookie':'guest_id=v1%3A140119213358937892; eu_cn=1; __utma=43838368.1474772765.1404091541.1405064347.1405064347.1; __utmz=43838368.1405064347.1.1.utmcsr=sublimetexttips.com|utmccn=(referral)|utmcmd=referral|utmcct=/giveaways/sublime-text-giveaway/; __utmv=43838368.lang%3A%20zh-cn; pid="v3:1405656201197878606892863"; remember_checked_on=1; auth_token=91a006e1fa442baf48e9840baec04e593faaa914; webn=1112070588; _gat=1; lang=zh-cn; goth=1; _ga=GA1.2.1474772765.1404091541; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCF5pYxBIAToMY3NyZl9p%250AZCIlNzY3MGE4NmNiMWRhMDhmZGZlOTc5OTg5NDVjZGE5Nzc6B2lkIiU1MzQx%250AN2UwNjk0ZDAwNDg3OGY2Y2MyM2EwYmVmMTJiYw%253D%253D--a2aee62e627cc83389c377790da13e304aa79e9e'}

i = 0

for line in file:

	urls = re.findall('https?://.*?\s', line)

	j = 0

	for url in urls:

		if ('…'.decode('utf-8') in url) or ('@' in url) or ('"' in url) or ('”'.decode('utf-8') in url):

			urls.remove(url)

		response = requests.get(url, params = payload)

		file = codecs.open(str(i) + str(j) + '.html', 'w', 'utf-8')

		file.write(response.text)

		file.close()

		j = j + 1

	i = i + 1
		
	print '\r\n'.join(urls)
