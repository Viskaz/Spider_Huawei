import re
from bs4 import BeautifulSoup


def loadfile(filepath):
    soup = BeautifulSoup(open(filepath), "lxml")
    titleList=[]
    for title in soup.find_all("th"):
        titleList.append(title.string)
    print(titleList)

    data_list = []
    for idx, tr in enumerate(soup.find_all('tr')):
        if idx != 0:
            tds = tr.find_all('td')
            i =0
            for title in titleList:
                data_list.append({
                    title:tds[i].contents[0]
                })
                i=i+1


    print(data_list)


if __name__ =='__main__':
    loadfile('data/table_test.html')
    # loadfile('data/structure.html')
