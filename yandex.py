import requests
import sys
import pyshorteners as sh

if len(sys.argv) < 2:
    print("You must specify an URL.")
    sys.exit(-1)
HostUrl = sys.argv[1]
try:
	searchUrl = 'https://yandex.com/images/search?rpt=imageview&url='+ HostUrl
	r = requests.post(url=searchUrl)
	x = r.url
	print(r)
	print(x)
	s = sh.Shortener()
	print(s.tinyurl.short(x))
except Exception as e:
	print(e)
	print(e.with_traceback)
