from bs4 import BeautifulSoup
from urllib import request
from you_get import common as you_get
import os
import sys
import time

json_file_path = ""
rank_link = "https://www.bilibili.com/ranking/rookie/0/0/3"
dir =os.path.abspath('.') + r"\videos"


#def store_av_numbers():


#def eliminate_repeat_av_numbers():

def find_av_numbers():
    avnumbers = []
    req = request.Request(rank_link)
    webpage = request.urlopen(req)
    html = webpage.read()
    soup = BeautifulSoup(html, 'html.parser')
    for k in soup.find_all(name = 'div', attrs={'class': 'info'}):
        link_to_video = k.a['href']
        for i in range(len(link_to_video) - 1, -1, -1):
            if link_to_video[i] is '/':
                avnumbers.append(link_to_video[i+1:int(len(link_to_video))])
                break
    return avnumbers


def downloadvideos(avnumbers):
    for avnumber in avnumbers:
        filename = time.strftime('%Y-%m-%d',time.localtime(time.time())) + "_" + avnumber
        weblink = "https://www.bilibili.com/video/" + avnumber + "/"
        sys.argv = ['you-get','-o',dir,'--output-filename',filename ,weblink]
        you_get.main()


if __name__=="__main__":
    opener = request.build_opener()
    opener.addheaders = [('User-agent',
                          'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10')]
    request.install_opener(opener)
    avnumbers = find_av_numbers()
    downloadvideos(avnumbers)
    print(find_av_numbers())