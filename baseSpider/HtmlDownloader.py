# -*-coding:utf-8-*-
#@Author: Songzq
#@Time: 2020年03月12日15时
import requests

class HtmlDownloader(object):

    def  download(self, url):
        if url is None:
            return None
        user_agent = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)

        if r.status_code==200:
            r.encoding='utf-8'
            return r.text
        return None