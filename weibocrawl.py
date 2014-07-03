import requests
import json

ACCESS_TOKEN = '2.00k72nYDlibo8D26fd23e4fdMiamCC'

BASE_URL = "https://api.weibo.com/2/"

params = {'address':address}

longitude = 0

latitude = 0

starttime = 1388505600							# unix timestamp

endtime = 0								# unix timestamp

RANGE = 11132								# the max range define in sina weibo api

sort = 0								# sort by time or sort by distance

COUNT = 50								# the count of items returned each time
 

params = {'access_token':,
	  'lat':latitude,
	  'long':longitude,
	  'range':
