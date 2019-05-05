import re
import read_write
from bs4 import BeautifulSoup

read_write_tem = read_write.Read_write()


def split_product_tables(source_file_path, result_file_path, one_product_divID):
    soup = BeautifulSoup(open(source_file_path), "lxml")
    a = soup.tbody.children
    line = soup.thead.tr
    reg = re.compile(("<[^>]*>"))

    one_product_all_information = soup.find(attrs={"id": one_product_divID})
    # 找到这个产品的名字，并且生成新的路径
    print("-------------------------------------------------------------------")
    file_id_tem = one_product_divID[7:]
    print("product section:" + file_id_tem)
    name = one_product_all_information.find('title').string
    result_file_path = result_file_path + file_id_tem + "_" + name + ".xlsx"
    print(name)
    # 创建一个execel表格
    read_write_tem.creat_excel_file(result_file_path)
    # 将产品信息通过section分开

    # one_product_sections_information = one_product_all_information.find(attrs={"class": "articleBox"})
    # sectionTabs = one_product_sections_information.find_all(attrs={"class": "sectionTab"}, limit=7)
    sectionTabs = one_product_all_information.find_all(attrs={"class": "sectionTab"})
    index = 0
    for one_section in sectionTabs:
        index += 1
        # if index == 6:
        #     continue
        all_table = one_section.find_all("table")
        for one_table in all_table:
            row_titles = []
            one_table_titles = one_table.thead.tr
            sheet_name = one_table.find("caption")
            sheet_name = reg.sub('', str(sheet_name)).replace(" ", "_").replace("/", "")
            if sheet_name == 'None' and index == 3:
                sheet_name = "后面板"
            # sheet_name = sheet_name[3:]
            print("********************************")
            print(sheet_name)

            # 提取表头
            for title in one_table_titles.stripped_strings:
                title_str = reg.sub('', str(title))
                row_titles.append(title_str)
            print(row_titles)

            read_write_tem.create_sheet(result_file_path, sheet_name, row_titles)

            one_table_contents = one_table.tbody.children
            row0 = []  # row0用于保存上一行的信息
            flag = True  # row0未初始化
            contents_rows = []  # 用于存储表格信息

            for child in one_table_contents:
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
                        read_write_tem.append_excel_xlsx(result_file_path, sheet_name, listTem)
                        print(listTem)
                    else:
                        contents_rows.append(row)
                        row0 = row  # 把本行的信息保存到上一行
                        listTem = list(filter(None, row))
                        read_write_tem.append_excel_xlsx(result_file_path, sheet_name, listTem)
                        print(listTem)


if __name__ == '__main__':

    # 接下来爬取5700，6700系列的表
    source_file_path_S600E = "./USG6000E.html"
    result_file_path_S600E = "./result-data/USG6000E/"
    all_product_divID = {"section3.2.1.1.1", "section3.2.1.1.2", "section3.2.1.1.3", "section3.2.1.1.4",
                         "section3.2.1.1.5", "section3.2.1.1.6", "section3.2.1.1.7", "section3.2.1.1.8"}

    for one_product_divID in all_product_divID:
        split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID)
