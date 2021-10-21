import urllib.request
import re
import json
import requests
import simplejson
import youtube_dl
import yt_dlp

html = urllib.request.urlopen("https://www.youtube.com/results?search_query=yeat")
string = html.read().decode()
index = 0
results = re.findall(r"watch\?v=(\S{11})", string);


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
ydl =  yt_dlp.YoutubeDL(ydl_opts)

for index, video in enumerate(results):
    if index != 5:
        with ydl:
            result = ydl.extract_info(
            'http://www.youtube.com/watch?v=' + video,
            download=False
            )
        if 'entries' in result:
            # Can be a playlist or a list of videos
            title = result['entries'][0]
        else:
            # Just a video
            title = result['title']
        print(title)
    else:
        break

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=' + results[0]])
