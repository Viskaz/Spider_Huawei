import re
import read_write
from bs4 import BeautifulSoup

read_write_tem = read_write.Read_write()



def split_product_tables(source_file_path,result_file_path,result_sheet_name):
    soup = BeautifulSoup(open(source_file_path), "lxml")

    reg = re.compile(("<[^>]*>"))

    # 找到一个产品所有table信息
    all_table_information = soup.find_all(attrs={"class": "tableBorder"})

    for one_table_information in all_table_information:

        # 创建一个Excel 表格
        read_write_tem.creat_excel_file(result_file_path)
        row_titles = []
        row0 = []  # row0用于保存上一行的信息
        flag = True  # row0未初始化
        contents_rows = []  # 用于存储表格信息
        one_table_titles = one_table_information.table.thead.tr
        one_table_contents = one_table_information.table.tbody.children

        # 提取表头
        for title in one_table_titles.stripped_strings:
            title_str = reg.sub('', str(title))
            row_titles.append(title_str)
        print(row_titles)
        read_write_tem.create_sheet(result_file_path, result_sheet_name, row_titles)
        print("********************************")
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
                    read_write_tem.append_excel_xlsx(result_file_path, result_sheet_name, listTem)
                    print(listTem)
                else:
                    contents_rows.append(row)
                    row0 = row  # 把本行的信息保存到上一行
                    listTem = list(filter(None, row))
                    read_write_tem.append_excel_xlsx(result_file_path, result_sheet_name, listTem)
                    print(listTem)


if __name__ == '__main__':


    source_file_path_8_2_2_1 = "./final-Data/8-2-2productDescription/8-2-2-1ProductRelationDescription.html"
    result_file_path_8_2_2_1="./final-Data/resultData/8-2-2产品描述/8-2-2-1ProductRelationDescription.xlsx"
    result_sheet_name_8_2_2_1 = "产品配套关系说明"
    split_product_tables(source_file_path_8_2_2_1,result_file_path_8_2_2_1, result_sheet_name_8_2_2_1)



    source_file_path_8_2_2_2 = "./final-Data/8-2-2productDescription/8-2-2-2ProductDescription.html"
    result_file_path_8_2_2_2 = "./final-Data/resultData/8-2-2产品描述/8-2-2-2ProductDescription.xlsx"
    result_file_name_8_2_2_2 = "8-2-2-2Description"
    result_sheet_name_8_2_2_2 = "产品概述"
    split_product_tables(source_file_path_8_2_2_2, result_file_path_8_2_2_2, result_sheet_name_8_2_2_2)


    source_file_path_8_2_2_5= "./final-data/8-2-2productDescription/8-2-2-5CharacteristicsSupportList.html"
    result_file_path_8_2_2_5 = "./final-Data/resultData/8-2-2产品描述/8-2-2-5CharacteristicSupportList.xlsx"
    result_file_name_8_2_2_5 = "8-2-2-5CharacteristicSupportList"
    result_sheet_name_8_2_2_5 = "特性支持列表"
    split_product_tables(source_file_path_8_2_2_5, result_file_path_8_2_2_5, result_sheet_name_8_2_2_5)