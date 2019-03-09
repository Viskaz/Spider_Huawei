# coding=UTF-8

import DAO.mySQL_operation
import read_write


def insert_table_information(file_path, sheet_name):
  db = DAO.mySQL_operation.MySQLOperation()
  list_tem = []
  read_write_tem = read_write.Read_write()
  list_tem = read_write_tem.read_excel_xlsx(file_path,sheet_name)
  del list_tem[0]
  for row in list_tem:
      print(row[0]+" "+row[1]+" "+row[2])
      print()
      db.insert_product(row[0],row[1],row[2])




if __name__ == '__main__':

  # t.seach_all()

  # t.insert_name("PWR：电源模块状态指示灯","绿色","常亮：表示所有的电源模块工作正常。")
  insert_table_information("/Users/viskaz/Documents/Pycharm-workSpace/Spider_Huawei/HuaweiProduct/CE12804.xlsx","表1 眉头指示灯的状态表")

