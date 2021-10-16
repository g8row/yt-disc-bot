import urllib.request
import re
import json
import requests
import simplejson


html = urllib.request.urlopen("https://www.youtube.com/results?search_query=yeat")
string = html.read().decode()
index = 0
for video in re.findall(r"watch\?v=(\S{11})", string):   
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % video}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string
    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        print(data['title'])


