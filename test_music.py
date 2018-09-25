import requests
import re
import urllib
import urllib.request
import json

#根据歌名查找
url_base = 'http://tingapi.ting.baidu.com/v1/restserver/ting?from=android&version=5.0.0.3&method=baidu.ting.search.catalogSug&format=json&query=%s'
#根据id查找
url_down = 'http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&songid=%s&_=1513517334915'

def getsonginfo(songs):
    url = url_base%(songs)
    # print(url)
    response = requests.get(url,verify=False)
    response.encoding = 'utf-8'
    content = response.text
    # print(content)
    songs_json = json.loads(content)
    # print(songs_json)
    songs_fo = songs_json["song"]
    # print(songs_fo)
    data = []
    for i in songs_fo:
        # print(i["songname"],songs)
        if i["songname"] == songs:
            songid = i["songid"]
            data.append(songid)
            # print(songid)
    # print(data)
    return data

def downloadmusic(songs_list):
    data = []
    for i in songs_list:
        url = url_down%(i)
        # print(url)
        response = requests.get(url, verify=False)
        response.encoding = 'utf-8'
        content = response.text
        # print(content)
        songs_json = json.loads(content)
        # print(songs_json)
        song_down_url = songs_json["bitrate"]["show_link"]
        data.append(song_down_url)
        # print(song_down_url)
    # print(data)
    return data

if __name__ == '__main__':
    n=0
    songs = input('请输入歌名：')
    #查找歌曲信息
    songs_list = getsonginfo(songs)
    song_url_list = downloadmusic(songs_list)
    for i in song_url_list:
        if n == 0:
            urllib.request.urlretrieve(url=i, filename='./music/%s.mp3' % (songs))
            print('歌曲<%s>下载成功！' % (songs))
            n+=1
        else:
            urllib.request.urlretrieve(url=i, filename='./music/%s%d.mp3' % (songs,n))
            print('歌曲<%s>%d下载成功！' % (songs, n))
            n+=1