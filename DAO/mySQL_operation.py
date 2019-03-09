import pymysql

class MySQLOperation:



    # 1.查询操作
    # 编写sql 查询语句  user 对应我的表名
    def seach_all(self):

        db = pymysql.connect(host="localhost", user="root",
                             password="123456", db="Huawei_product", port=3306)
        cur = db.cursor()
        sql = "select * from test"
        try:
            cur.execute(sql)  # 执行sql语句

            results = cur.fetchall()  # 获取查询的所有记录
            print("id", "name")
            # 遍历结果
            for row in results:
                id = row[0]
                name = row[1]
                print(id, name)
        except Exception as e:
            raise e
        finally:
            db.close()


    def insert_product(self,light,color,meaning):

        db = pymysql.connect(host="localhost", user="root",
                             password="123456", db="Huawei_product", port=3306)
        cur = db.cursor()
        sql_insert = "insert into CE12804(light,color,meaning) values('%s','%s','%s')"%(light,color,meaning)
        # print(sql_insert)

        try:
            cur.execute(sql_insert)
            # 提交
            db.commit()
        except Exception as e:
            # 错误回滚
            db.rollback()
        finally:
            db.close()