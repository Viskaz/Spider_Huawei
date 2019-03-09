import re
import read_write
from bs4 import BeautifulSoup

read_write_tem = read_write.Read_write()
source_file_path = "./semi_structure.html"
result_file_path = "./semi_structure.xlsx"
result_sheet_name = "sheet1"


def load_file(filepath):
    soup = BeautifulSoup(open(filepath), "lxml")
    a = soup.tbody.children
    line = soup.thead.tr



    reg = re.compile(("<[^>]*>"))  # 清除html标签,提取文本
    row0 = []  # row0用于保存上一行的信息
    flag = True  # row0未初始化
    row_titles = []
    contents_rows =[] # 用于存储表格信息

    # 提取表头
    for title in line.stripped_strings:
        print(title)
        title_str = reg.sub('', str(title))
        row_titles.append(title_str)
    print(row_titles)
    read_write_tem.write_excel_xlsx(result_file_path, result_sheet_name, row_titles)


    for child in a:
        row = []  # 保存表格提取结果

        if child.find('th'):
            continue
        if child.find('td'):  # 提取每一行
            for value in child.children:
                st = reg.sub('', str(value))
                row.append(st.strip('\n'))
            if flag:
                flag = False
            if len(row) < len(row0):  # 与上一行比较,分析是否需要处理字段缺省的情况
                row_temp = row0[0:len(row0) - len(row)]
                for i in range(len(row)):
                    row_temp.append(row[i])
                row0 = row_temp
                row = row_temp
                contents_rows.append(row)
                listTem = list(filter(None, row))
                read_write_tem.append_excel_xlsx(result_file_path,result_sheet_name,listTem)
                print(listTem)
            else:
                contents_rows.append(row)
                row0 = row  # 把本行的信息保存到上一行
                listTem=list(filter(None,row))
                read_write_tem.append_excel_xlsx(result_file_path, result_sheet_name, listTem)
                print(listTem)



if __name__ == '__main__':
    load_file(source_file_path)
