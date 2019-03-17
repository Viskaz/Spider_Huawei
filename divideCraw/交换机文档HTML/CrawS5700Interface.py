import re
import read_write
from bs4 import BeautifulSoup

read_write_tem = read_write.Read_write()

result_file_name = "8-2-2-3ProductAppearance"
result_sheet_name = "产品配套关系说明"


def split_product_tables(source_file_path, result_file_path, one_product_divID, sheet1_name, sheet2_name,
                         sheet3_name):
    soup = BeautifulSoup(open(source_file_path), "lxml")
    a = soup.tbody.children
    line = soup.thead.tr
    reg = re.compile(("<[^>]*>"))

    # 创建一个execel表格
    read_write_tem.creat_excel_file(result_file_path)
    # 将产品信息通过section分开
    one_product_all_information = soup.find(attrs={"id": one_product_divID})

    one_product_sections_information = one_product_all_information.find(attrs={"class": "articleBox"})
    sectionTabs = one_product_sections_information.find_all(attrs={"class": "sectionTab"}, limit=3)

    index = 0
    for one_section in sectionTabs:
        index += 1
        if index < 3:
            continue
        all_table = one_section.find_all("table")
        # print(all_table)
        table_index = 1
        for one_table in all_table:
            row_titles = []
            contents_rows = []
            one_table_titles = one_table.thead.tr
            one_table_contents = one_table.tbody.children

            # 提取表头
            for title in one_table_titles.stripped_strings:
                title_str = reg.sub('', str(title))
                row_titles.append(title_str)
            print(row_titles)
            global sheet_name
            if table_index == 1:
                sheet_name = sheet1_name
            elif table_index == 2:
                sheet_name = sheet2_name
            elif table_index == 3:
                sheet_name = sheet3_name
            table_index = table_index + 1
            print("sheet name is:" + sheet_name)
            print("table index is " + str(table_index))

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

    #这个一直爬取到section 7.3.4.6.14

    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-12TP-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.1"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-12TP-PWR-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.2"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28TP-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.3"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28TP-PWR-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.4"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28TP-PWR-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.5"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28P-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.6"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28P-PWR-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.7"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-52P-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.8"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-52P-PWR-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.9"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-16X-PWH-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.10"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28X-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.11"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28X-LI-DC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.12"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28X-LI-24S-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.13"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28X-LI-24S-DC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.14"
    # sheet1_name = "100_1000BASE-X以太网接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28X-PWR-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.15"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28X-PWR-LI-ACF_interface.xlsx"
    # one_product_divID = "section7.3.4.5.16"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-28X-PWH-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.17"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "100M_1000M_2.5GE BASE-T以太网电接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-52X-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.18"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/5720-52X-LI-DC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.19"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-52X-PWR-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.20"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-52X-PWR-LI-ACF_interface.xlsx"
    # one_product_divID = "section7.3.4.5.21"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720-52X-LI-48S-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.5.22"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #######################################################################################
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720S-12TP-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.1"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720S-12TP-PWR-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.2"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720S-28TP-PWR-LI-ACL_interface.xlsx"
    # one_product_divID = "section7.3.4.6.3"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720S-28P-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.4"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720SV2-28P-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.5"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720S-28P-PWR-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.6"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720S-52P-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.7"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720SV2-52P-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.8"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720S-52P-PWR-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.9"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "1000BASE-X以太网光接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720S-28X-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.10"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720S-28X-LI-24S-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.11"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720S-28X-PWR-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.12"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    # source_file_path_S600E = "./S2720_S5700_S6720.html"
    # result_file_path_S600E = "./result-data/S5700/S5720S-52X-LI-AC_interface.xlsx"
    # one_product_divID = "section7.3.4.6.13"
    # sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    # sheet2_name = "10GE_SFP以太网接口属性"
    # sheet3_name = "Console接口属性"
    # split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
    #                      sheet1_name, sheet2_name, sheet3_name)
    #
    source_file_path_S600E = "./S2720_S5700_S6720.html"
    result_file_path_S600E = "./result-data/S5700/S5720S-52X-PWR-LI-AC_interface.xlsx"
    one_product_divID = "section7.3.4.6.14"
    sheet1_name = "10_100_1000BASE-T以太网电接口属性"
    sheet2_name = "10GE_SFP以太网接口属性"
    sheet3_name = "Console接口属性"
    split_product_tables(source_file_path_S600E, result_file_path_S600E, one_product_divID,
                         sheet1_name, sheet2_name, sheet3_name)