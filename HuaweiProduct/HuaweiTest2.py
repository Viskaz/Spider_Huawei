import re
import read_write
from bs4 import BeautifulSoup

read_write_tem = read_write.Read_write()

source_file_path = "./CloudEngine.html"

reg_rm_symbol_in_execel=re.compile("/")





def split_product_tables(filepath):
    soup = BeautifulSoup(open(source_file_path), "lxml")
    a = soup.tbody.children
    line = soup.thead.tr
    reg = re.compile(("<[^>]*>"))


    # 将产品信息通过section分开
    product_all_product_list = soup.find_all(id=re.compile("section8."))
    for one_product in product_all_product_list:
        one_product_name = one_product.find('a').get('name')
        one_product_file_name = one_product_name +'.xlsx'

        # 为每个型号的产品创建一个execel表格
        read_write_tem.creat_excel_file(one_product_file_name)

        print(one_product_file_name)



        # 找到一个产品所有table信息
        all_table_information = one_product.find_all(attrs={"class": "tableBorder"})

        for one_table_information in all_table_information:
            one_table_sheet_name = one_table_information.find('table').find('caption')
            one_table_sheet_name = reg.sub('', str(one_table_sheet_name))
            one_table_sheet_name = reg_rm_symbol_in_execel.sub('-',str(one_table_sheet_name))
            if one_table_sheet_name == 'None':
                print('empty')
                one_table_sheet_name = one_table_information.previous_element.previous_element
                if not one_table_sheet_name.strip()=='':
                    print(one_table_sheet_name)
                else:
                    print("没有找到表格名字")

            else:
                print(one_table_sheet_name)

            if not one_table_sheet_name.strip()=='':
                row_titles = []
                contents_rows = []
                one_table_titles=one_table_information.table.thead.tr
                one_table_contents=one_table_information.table.tbody.children

                # 提取表头
                for title in one_table_titles.stripped_strings:
                    title_str = reg.sub('', str(title))
                    row_titles.append(title_str)
                print(row_titles)
                read_write_tem.create_sheet(one_product_file_name,one_table_sheet_name,row_titles)
                print("********************************")

                one_table_contents=one_table_information.table.tbody.children
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
                            read_write_tem.append_excel_xlsx(one_product_file_name, one_table_sheet_name, listTem)
                            print(listTem)
                        else:
                            contents_rows.append(row)
                            row0 = row  # 把本行的信息保存到上一行
                            listTem = list(filter(None, row))
                            read_write_tem.append_excel_xlsx(one_product_file_name, one_table_sheet_name, listTem)
                            print(listTem)












if __name__ == '__main__':
    split_product_tables(source_file_path)
