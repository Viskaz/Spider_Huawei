import re
import read_write
from bs4 import BeautifulSoup

read_write_tem = read_write.Read_write()
source_file_path = "./8-3-3-2-3-1机框分类详述.html"
result_file_path_tem = "./8-3-3-2-3-1机框"
result_file_name = "8-2-2-3ProductAppearance"

result_sheet_name = "产品配套关系说明"
product_list = ["CE12804", "CE12808", "CE12812", "CE12816", "CE12804S", "CE12808S"]


def split_product_tables():
    soup = BeautifulSoup(open(source_file_path), "lxml")

    reg = re.compile(("<[^>]*>"))

    # 将产品信息通过section分开
    all_product_information_list = soup.find_all(attrs={"class": "articleBox"})

    i = 0
    for one_product in all_product_information_list:
        if i > 5:
            break
        product_name = product_list[i]
        i += 1

        one_product_result_path = result_file_path_tem + product_name + ".xlsx"
        # 为每个产品创建一个excel表格
        read_write_tem.creat_excel_file(one_product_result_path)
        # 找到一个产品所有table信息
        one_product_information = one_product.find(attrs={"class": "tableBorder"})

        # one_product_sheet_name = one_product_information.find('caption')
        one_product_sheet_name = "sheets"+str(i)
        print(one_product_sheet_name)

        row_titles = []
        contents_rows = []
        one_table_titles = one_product_information.table.thead.tr

        one_table_contents = one_product_information.table.tbody.children

        # 提取表头
        for title in one_table_titles.stripped_strings:
            title_str = reg.sub('', str(title))
            row_titles.append(title_str)
        print(row_titles)
        read_write_tem.create_sheet(one_product_information, one_product_sheet_name, row_titles)
        print("********************************")

        one_table_contents = one_product_information.table.tbody.children
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
                    read_write_tem.append_excel_xlsx(one_product_result_path, one_product_sheet_name, listTem)
                    print(listTem)
                else:
                    contents_rows.append(row)
                    row0 = row  # 把本行的信息保存到上一行
                    listTem = list(filter(None, row))
                    read_write_tem.append_excel_xlsx(one_product_result_path, one_product_sheet_name, listTem)
                    print(listTem)


if __name__ == '__main__':
    split_product_tables()
