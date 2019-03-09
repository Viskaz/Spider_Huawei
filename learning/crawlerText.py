# _*_ encoding:utf-8 _*_
from bs4 import BeautifulSoup
import  requests
import  time
import json
import sys
#设置系统默认编码模式，如果不设置可能写入文件会报错
reload(sys)
sys.setdefaultencoding('utf8')

sArticle =""
#urlcontent 为爬取小说内容的url
urlcontent ="https://m.qidian.com/book/{}/{}".format("1003782761","321319656")
#url为获取下一章节id的url,通过requesturl获得
url = "https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=w7RePr18qXzxByPdIn0h7iQtII0AC4z8oPMIXioz&bookId={}&chapterId={}".format("1003782761","321319656")
#保存爬取的小说内容
f = open('C:\Users\Administrator\Desktop\\test.txt', 'w')


def xiaoshuo(url,urlcontent,sArticle):
    wb_data = requests.get(url)
    soup =BeautifulSoup(wb_data.text,'lxml')
    wb_Content = requests.get(urlcontent)
    soupContent =BeautifulSoup(wb_Content.text,'lxml')
    title = soupContent.select("#chapterContent > section > h3")
    article = soupContent.select("#chapterContent > section > p")
    print title[0].get_text()
  #为了方便阅读标题后加入换行
    f.writelines(str(title[0].get_text()) + "\n")
    for p in article:
        sArticle +=p.get_text()
        #为了阅读方便每一段加一个换行
        f.writelines(str(p.get_text())+"\n")

    print sArticle
    #字符串转化json格式
    jsonStr = json.loads(soup.text)

    nextCharId=jsonStr["data"]["chapterInfo"]["next"]
    print(nextCharId)
    return nextCharId
#例子获取从第四章开始的后五篇小说
for i in range(5):
    nextId = xiaoshuo(url, urlcontent, sArticle)
    urlcontent = "https://m.qidian.com/book/{}/{}".format("1003782761", nextId)
    url = "https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=w7RePr18qXzxByPdIn0h7iQtII0AC4z8oPMIXioz&bookId={}&chapterId={}".format("1003782761", nextId)
    sArticle =""
f.close()
