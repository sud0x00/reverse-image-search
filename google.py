import requests
import sys
import pyshorteners as sh

if len(sys.argv) < 2:
    print("You must specify a file name.")
    sys.exit(-1)
filePath = sys.argv[1]
try:
    searchUrl = 'http://www.google.com/searchbyimage/upload'
    multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']
    print(response)
    print(fetchUrl)
    s = sh.Shortener()
    print(s.tinyurl.short(fetchUrl))
except Exception as e:
    print(e)
    print(e.with_traceback)
