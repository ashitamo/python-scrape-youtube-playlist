from bs4 import BeautifulSoup as bs4
import requests
import re
import json,youtube_dl,datetime
headers= {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
class YT(object):
    @staticmethod
    def yt(url):
        back=[]
        if re.match(r'https://www.youtube.com/watch\?v=[a-zA-Z0-9]+&list=[a-zA-Z0-9]',url):
            a=re.search(r'https://www.youtube.com/watch\?v=[a-zA-Z0-9]+&list=[a-zA-Z0-9]+&index=(.*)',url)
            b=re.search(r'https://www.youtube.com/watch\?v=[a-zA-Z0-9]+&list=[a-zA-Z0-9]+&index=(.*)&',url)
            if a or b:
                try:
                    counter=int(a.group(1))
                except:
                    counter=int(b.group(1))
            else:
                counter=1
            res= requests.get(url)
            soup=bs4(res.text, 'html.parser')
            aid=soup.find('script',string=re.compile('ytInitialData'))
            scrip=str(aid).replace('<script>\n    window["ytInitialData"] = ','').split(';')
            try:
                #print(scrip,len(scrip))
                js=json.loads(scrip[0]+scrip[1])
            except:
                try:
                    js=json.loads(scrip[0])
                except:
                    js=json.loads(scrip[0]+scrip[1]+scrip[2])
            a=js['contents']['twoColumnWatchNextResults']["playlist"]["playlist"]['contents']
            listTitle=js['contents']['twoColumnWatchNextResults']["playlist"]["playlist"]['title']
            for i in a:
                videoId=i['playlistPanelVideoRenderer']['videoId']
                try:
                    title=i['playlistPanelVideoRenderer']['title']['simpleText']
                    duration=i['playlistPanelVideoRenderer']['lengthText']['simpleText']
                except:
                    title='已刪除影片'
                    song_duration='00:00'
                detail=[videoId,title,duration]
                back.append(detail)
            # i=back[counter-1]
            # del back[counter-1]
            # back.insert(0,back[counter-1])

        #
        elif re.match('https://www.youtube.com/playlist\?list=',url):
            searched=requests.get(url,headers=headers)
            soup=bs4(searched.text,'html.parser')
            aid=soup.find('script',string=re.compile('ytInitialData'))
            scrip=str(aid).replace('<script>\n    window["ytInitialData"] = ','').split(';')
            listTitle=soup.title.string.replace(' - YouTube','')
            for i in range(1,4,1):
                del scrip[-1]
            #print(len(scrip))
            js=json.loads(scrip[0])
            a=js['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['playlistVideoListRenderer']['contents']
            for i in a:
                videoId=i['playlistVideoRenderer']['videoId']
                try:
                    title=i['playlistVideoRenderer']['title']['simpleText']
                    song_duration=i['playlistVideoRenderer']['lengthText']['simpleText']
                except KeyError:
                    title='已刪除影片'
                    song_duration='00:00'
                detail=[videoId,title,song_duration]
                back.append(detail)
        #print(back)
        return listTitle,back