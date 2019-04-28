import re
import read_write
from bs4 import BeautifulSoup

read_write_tem = read_write.Read_write()

result_file_name = "8-2-2-3ProductAppearance"
result_sheet_name = "产品配套关系说明"


def split_product_tables(source_file_path, result_file_path, one_product_divID):
    soup = BeautifulSoup(open(source_file_path), "lxml")
    a = soup.tbody.children
    line = soup.thead.tr
    reg = re.compile(("<[^>]*>"))

    one_product_all_information = soup.find(attrs={"id": one_product_divID})
    # 找到这个产品的名字，并且生成新的路径
    name = one_product_all_information.find('title').string
    result_file_path = result_file_path + name + "_interface.xlsx"
    print(name)
    # 创建一个execel表格
    read_write_tem.creat_excel_file(result_file_path)
    # 将产品信息通过section分开

    one_product_sections_information = one_product_all_information.find(attrs={"class": "articleBox"})
    sectionTabs = one_product_sections_information.find_all(attrs={"class": "sectionTab"}, limit=3)

    index = 0
    for one_section in sectionTabs:
        index += 1
        if index < 3:
            continue
        all_table = one_section.find_all("table")
        for one_table in all_table:
            row_titles = []
            one_table_titles = one_table.thead.tr
            sheet_name = one_table.find("caption")
            sheet_name = reg.sub('', str(sheet_name)).replace(" ", "_").replace("/", "")

            print(sheet_name)

            # 提取表头
            for title in one_table_titles.stripped_strings:
                title_str = reg.sub('', str(title))
                row_titles.append(title_str)
            print(row_titles)

            read_write_tem.create_sheet(result_file_path, sheet_name, row_titles)
            print("********************************")

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
    source_file_path_S600E = "./S2720_S5700_S6720.html"
    result_file_path_S600E = "./result-data/S5700X/"
    all_product_divID = {"section7.3.4.7.1", "section7.3.4.7.2", "section7.3.4.7.3", "section7.3.4.7.4",
                         "section7.3.4.7.5", "section7.3.4.7.6", "section7.3.4.7.7", "section7.3.4.7.8",
                         "section7.3.4.7.9", "section7.3.4.7.10", "section7.3.4.7.11", "section7.3.4.7.12",
                         "section7.3.4.7.13", "section7.3.4.7.14", "section7.3.4.7.15", "section7.3.4.7.16"}
    # all_product_divID = {"section7.3.4.8.1","section7.3.4.8.2","section7.3.4.8.3","section7.3.4.8.4",
    #                      "section7.3.4.8.5","section7.3.4.8.6","section7.3.4.9.1","section7.3.4.9.2",
    #                      "section7.3.4.9.3","section7.3.4.9.4","section7.3.4.9.5","section7.3.4.9.6",
    #                      "section7.3.4.10.1","section7.3.4.10.2","section7.3.4.10.3","section7.3.4.10.4",
    #                      "section7.3.4.10.5"}
    # all_product_divID = {"section7.3.4.11.1","section7.3.4.11.2","section7.3.4.11.3","section7.3.4.11.4",
    #                      "section7.3.4.11.5","section7.3.4.11.6","section7.3.4.11.7","section7.3.4.11.8",
    #                      "section7.3.4.11.9","section7.3.4.11.10","section7.3.4.11.11","section7.3.4.11.12",
    #                      "section7.3.4.11.13","section7.3.4.11.14","section7.3.4.11.15","section7.3.4.11.16",
    #                      "section7.3.4.11.17","section7.3.4.11.18","section7.3.4.11.19","section7.3.4.11.20",
    #                      "section7.3.4.11.21","section7.3.4.11.22","section7.3.4.11.23","section7.3.4.11.24",
    #                      "section7.3.4.11.25","section7.3.4.11.26"}
    # all_product_divID = {"section7.3.4.12.1", "section7.3.4.12.2", "section7.3.4.12.3", "section7.3.4.12.4",
    #                      "section7.3.4.13.1", "section7.3.4.13.2", "section7.3.4.13.3", "section7.3.4.13.4",
    #                      "section7.3.4.14.1", "section7.3.4.14.2", "section7.3.4.14.3", "section7.3.4.14.4",
    #                      "section7.3.4.14.5", "section7.3.4.14.6", "section7.3.4.14.7", "section7.3.4.14.8",
    #                      "section7.3.4.14.9", "section7.3.4.14.10", "section7.3.4.14.11", "section7.3.4.14.12"}
    for one_product_divID in all_product_divID:
        split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID)
