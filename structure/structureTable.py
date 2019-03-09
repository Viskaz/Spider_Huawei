import re
from bs4 import BeautifulSoup
import read_write

readWriteTem = read_write.Read_write()


def loadfile(source_file, target_file, sheet_name):
    soup = BeautifulSoup(open(source_file), "lxml")
    title_list = []
    for title in soup.find_all("th"):
        title_string = title.get_text().strip('\n')
        title_list.append(title_string)
        print(title_string)
    print(title_list)
    readWriteTem.write_excel_xlsx(target_file, sheet_name, title_list)


    data_list = []
    for idx, tr in enumerate(soup.find_all('tr')):
        if idx != 0:
            tds = tr.find_all('td')
            i = 0
            for title in title_list:
                data_list.append({
                    title: tds[i].contents[0]
                })
                i = i + 1

    print(data_list)


if __name__ == '__main__':
    # loadfile('data/table_test.html')
    loadfile('data/structure.html', './structure/structureResult.xlsx', 'sheet1')
